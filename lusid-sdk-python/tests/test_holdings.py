import unittest
import requests
import json
import os
from datetime import datetime
import pytz
import lusid
import lusid.models as models
from unittest import TestCase
from msrest.authentication import BasicTokenAuthentication
from TestDataUtilities import TestDataUtilities
from InstrumentLoader import InstrumentLoader

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestHoldingsFinbourneApi(TestCase):
    client = None
    effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

    @classmethod
    def setUpClass(cls):

        cls.ISIN_PROPERTY_KEY = "Instrument/default/Isin"
        cls.SEDOL_PROPERTY_KEY = "Instrument/default/Sedol"
        cls.FIGI_SCHEME = "Figi"
        cls.CUSTOM_INTERNAL_SCHEME = "ClientInternal"
        cls.GROUPBY_KEY = "Instrument/default/Name"
        cls.AGGREGATION_KEY = "Holding/default/PV"
        cls.sorted_instrument_ids = []
        cls.SCOPE = "Finbourne"

        # Load our configuration details from the environment variables
        token_url = os.getenv("FBN_TOKEN_URL", None)
        cls.api_url = os.getenv("FBN_LUSID_API_URL", None)
        username = os.getenv("FBN_USERNAME", None)
        password_raw = os.getenv("FBN_PASSWORD", None)
        client_id_raw = os.getenv("FBN_CLIENT_ID", None)
        client_secret_raw = os.getenv("FBN_CLIENT_SECRET", None)

        # If any of the environmental variables are missing use a local secrets file
        if token_url is None or username is None or password_raw is None or client_id_raw is None \
                or client_secret_raw is None or cls.api_url is None:

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(dir_path, "secrets.json"), "r") as secrets:
                config = json.load(secrets)

            token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
            username = os.getenv("FBN_USERNAME", config["api"]["username"])
            password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
            client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
            client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
            cls.api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])

        else:
            password = pathname2url(password_raw)
            client_id = pathname2url(client_id_raw)
            client_secret = pathname2url(client_secret_raw)

        # Prepare our authentication request
        token_request_body = ("grant_type=password&username={0}".format(username) +
                              "&password={0}&scope=openid client groups".format(password) +
                              "&client_id={0}&client_secret={1}".format(client_id, client_secret))
        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # Make our authentication request
        okta_response = requests.post(token_url, data=token_request_body, headers=headers)

        # Ensure that we have a 200 response code
        assert okta_response.status_code == 200

        # Retrieve our api token from the authentication response
        cls.api_token = {"access_token": okta_response.json()["access_token"]}

        # Initialise our API client using our token so that we can include it in all future requests
        credentials = BasicTokenAuthentication(cls.api_token)
        cls.client = lusid.LUSIDAPI(credentials, cls.api_url)

        # Create and load in instruments

        cls.instrument_ids = InstrumentLoader.load_instruments(cls.client)

        # sort the instruments..ordered list of luids...
        for instrument in cls.instrument_ids.values:
            cls.sorted_instrument_ids.append(cls.instrument_ids.values[instrument].lusid_instrument_id)
        cls.sorted_instrument_ids.sort()

        assert len(cls.instrument_ids.values) == 5

    @classmethod
    def tearDownClass(cls):
        response = InstrumentLoader.delete_instruments(cls.client)

    def test_get_holdings(self):

        currency = "GBP"

        day0 = datetime(2018, 1, 1, tzinfo=pytz.utc)                # today
        day_tplus5 = datetime(2018, 1, 6, tzinfo=pytz.utc)           # t+5
        day_tplus10 = datetime(2018, 1, 11, tzinfo=pytz.utc)         # t+10

        # create the transactions
        tran_requests = []

        # create the portfolio and get the id code
        portfolio_code = TestDataUtilities.create_transaction_portfolio(self.client, self.SCOPE)
        # add the starting cash
        tran_requests.append(TestDataUtilities.build_cash_funds_in_transaction_request(units=100000.0,
                                                                                       currency=currency,
                                                                                       trade_date=day0))
        # create initial transactions
        idx = 0
        # we want to create transactions based on the first 3 instruments
        for idx in range(3):
            instrument = self.sorted_instrument_ids[idx]

            tran_requests.append(TestDataUtilities.build_transaction_request
                                 (instrument_id=instrument,
                                  units=100.0,
                                  price=101.0 + idx,
                                  currency=currency,
                                  trade_date=day0,
                                  transaction_type="Buy"))

        # on day 5, add a transaction using the 4th instrument [3], and increase the amount of the second [1]
        tran_requests.append(TestDataUtilities.build_transaction_request(
            instrument_id=self.sorted_instrument_ids[1],
            units=100.0,
            price=104.0,
            currency=currency,
            trade_date=day_tplus5,
            transaction_type="Buy"))
        tran_requests.append(TestDataUtilities.build_transaction_request(
            instrument_id=self.sorted_instrument_ids[3],
            units=100.0,
            price=105.0,
            currency=currency,
            trade_date=day_tplus5,
            transaction_type="Buy"))

        # add the trade
        upsert_response = self.client.upsert_transactions(self.SCOPE, portfolio_code, tran_requests)

        # get the t+10 holdings
        t10_holdings = self.client.get_holdings(self.SCOPE, portfolio_code, False, day_tplus10)

        t10_holdings.values = sorted(t10_holdings.values, key=lambda k: k.instrument_uid)

        assert t10_holdings.count == 5

        # cash balance
        assert t10_holdings.values[0].instrument_uid == "CCY_" + currency
        assert t10_holdings.values[0].holding_type == "B"
        assert t10_holdings.values[0].units == 48500.0

        # instrument holdings. Holding type "P" represents a position
        assert t10_holdings.values[1].instrument_uid == self.sorted_instrument_ids[0]
        assert t10_holdings.values[1].holding_type == "P"
        assert t10_holdings.values[1].units == 100.0
        assert t10_holdings.values[1].cost.amount == 10100.0

        assert t10_holdings.values[2].instrument_uid == self.sorted_instrument_ids[1]
        assert t10_holdings.values[2].holding_type == "P"
        assert t10_holdings.values[2].units == 200.0
        assert t10_holdings.values[2].cost.amount == 20600.0

        assert t10_holdings.values[3].instrument_uid == self.sorted_instrument_ids[2]
        assert t10_holdings.values[3].holding_type == "P"
        assert t10_holdings.values[3].units == 100.0
        assert t10_holdings.values[3].cost.amount == 10300.0

        assert t10_holdings.values[4].instrument_uid == self.sorted_instrument_ids[3]
        assert t10_holdings.values[4].holding_type == "P"
        assert t10_holdings.values[4].units == 100.0
        assert t10_holdings.values[4].cost.amount == 10500.0

    def test_set_target_holdings(self):

        currency = "GBP"

        day0 = datetime(2018, 1, 1, tzinfo=pytz.utc)                # today
        day_tplus5 = datetime(2018, 1, 6, tzinfo=pytz.utc)           # t+5

        # create the transactions
        tran_requests = []

        # create the portfolio and get the id code
        portfolio_code = TestDataUtilities.create_transaction_portfolio(self.client, self.SCOPE)

        cash_inst = "CCY_" + currency
        holding_adj = []

        # add the cash
        holding_adj.append(models.AdjustHoldingRequest(cash_inst, [models.TargetTaxLotRequest(100000.0)]))
        # instrument 1
        holding_adj.append(models.AdjustHoldingRequest(
            self.sorted_instrument_ids[0], [models.TargetTaxLotRequest(
                                                units=100.0,
                                                cost=models.CurrencyAndAmount(10100.0, currency),
                                                portfolio_cost=10100.0,
                                                price=101.0,
                                                purchase_date=day0,
                                                settlement_date=day0)]))

        holding_adj.append(models.AdjustHoldingRequest(
            self.sorted_instrument_ids[1], [models.TargetTaxLotRequest(
                                                units=100.0,
                                                cost=models.CurrencyAndAmount(10200.0, currency),
                                                portfolio_cost=10200.0,
                                                price=102.0,
                                                purchase_date=day0,
                                                settlement_date=day0)]))

        # set the initial holdings on day0
        set_holdings_response = self.client.set_holdings(self.SCOPE, portfolio_code, day0, holding_adj)

        # add subsequent transactions on t+5
        tran_requests.append(TestDataUtilities.build_transaction_request(
            self.sorted_instrument_ids[0],
            units=100.0,
            price=104.0,
            currency=currency,
            trade_date=day_tplus5,
            transaction_type="Buy"))

        tran_requests.append(TestDataUtilities.build_transaction_request(
            self.sorted_instrument_ids[2],
            units=100.0,
            price=103.0,
            currency=currency,
            trade_date=day_tplus5,
            transaction_type="Buy"))
        # add these transactions
        upsert_response = self.client.upsert_transactions(self.SCOPE, portfolio_code, tran_requests)

        # get the holdings for t+5

        t5_holdings = self.client.get_holdings(self.SCOPE, portfolio_code, False, day_tplus5)

        # sort
        t5_holdings.values = sorted(t5_holdings.values, key=lambda k: k.instrument_uid)

        # cash balance + 3 holdings
        assert t5_holdings.count == 4

        # remaining cash balance which takes into account the purchase transactions on day 2

        assert t5_holdings.values[0].instrument_uid == cash_inst
        assert t5_holdings.values[0].units == 79300.0

        # instrument1 initial holding + transaction on day t+5
        assert t5_holdings.values[1].instrument_uid == self.sorted_instrument_ids[0]
        assert t5_holdings.values[1].units == 200.0
        assert t5_holdings.values[1].cost.amount == 20500.0

        # instrument2 initial holding
        assert t5_holdings.values[2].instrument_uid == self.sorted_instrument_ids[1]
        assert t5_holdings.values[2].units == 100.0
        assert t5_holdings.values[2].cost.amount == 10200.0

        # instrument3 transactions on  t+5
        assert t5_holdings.values[3].instrument_uid == self.sorted_instrument_ids[2]
        assert t5_holdings.values[3].units == 100.0
        assert t5_holdings.values[3].cost.amount == 10300.0


if __name__ == '__main__':
    unittest.main()
