import unittest
import requests
import json
import uuid
import os
from datetime import datetime
import pytz
import lusid
import lusid.models as models
from unittest import TestCase
from collections import namedtuple
from msrest.authentication import BasicTokenAuthentication
from time import sleep
from TestDataUtilities import TestDataUtilities
from InstrumentLoader import InstrumentLoader

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestFinbourneApi(TestCase):
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
        cls.inst_loader = InstrumentLoader()
        cls.instrument_ids = cls.inst_loader.load_instruments(cls.client)
        # sort the instruments by instrument name to match the aggregation ordering later
        luids_to_sort = {}
        for instrument in cls.instrument_ids.values:
            luids_to_sort[cls.instrument_ids.values[instrument].lusid_instrument_id] = cls.instrument_ids.values[instrument].name
        cls.sorted_instrument_ids = sorted(luids_to_sort, key=luids_to_sort.__getitem__)
        assert len(cls.instrument_ids.values) == 5

    @classmethod
    def tearDownClass(cls):
        response = cls.inst_loader.tearDownClass(cls)

    def test_run_aggregation_with_buy(self):

        currency = "GBP"
        # create the transactions
        tran_requests = []

        test_utility = TestDataUtilities(self.client)
        # add the starting cash
        tran_requests.append(test_utility.build_cash_funds_in_transaction_request(units=51501.0,
                                                                                  currency=currency,
                                                                                  trade_date=self.effective_date))
        # create the transaction requests
        idx = 0
        for instrument in self.sorted_instrument_ids:
            idx = idx + 1
            tran_requests.append(test_utility.build_transaction_request(instrument_id=instrument,
                                                                        units=100.0,
                                                                        price=100.0 + idx,
                                                                        currency=currency,
                                                                        trade_date=self.effective_date,
                                                                        transaction_type="Buy"))

        response = self.run_aggregation(create_transaction_requests=tran_requests)
        # add in some error checks here?
        assert len(response) > 0
        assert response[0]["Sum(" + self.AGGREGATION_KEY + ")"] == 10000.0             # Barclays
        assert response[1]["Sum(" + self.AGGREGATION_KEY + ")"] == 20000.0             # National Grid
        assert response[2]["Sum(" + self.AGGREGATION_KEY + ")"] == 30000.0             # Sainsburys

    def run_aggregation(self, create_transaction_requests):

        uuid_gen = uuid.uuid4()
        scope = "finbourne"

        # build the create portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=self.effective_date)
        # create the portfolio
        portfolio_response = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio_response.id.code, request.code)

        portfolio_id = portfolio_response.id.code

        # build the transaction requests
        tran_req = []
        for i in create_transaction_requests:
            tran_req.append(i)

        # upload the transactions to LUSID
        upsert_response = self.client.upsert_transactions(scope, portfolio_id, tran_req)
        assert len(upsert_response.links) > 0
        # set up the prices used for the aggregation in the analytic stores
        # is there a store in the list on the effective date?
        analytic_stores = self.client.list_analytic_stores().values
        count = 0
        for store in analytic_stores:
            if store.date_property == self.effective_date:
                count = count + 1

        if count == 0:
            # create the analytic store
            response = self.client.create_analytic_store({"scope": scope, "date": self.effective_date})

        # create prices dictionary, add to an instrument analytic
        idx = 0
        instrument_analytic_list = []
        for instrument in self.sorted_instrument_ids:
            idx = idx + 1
            instrument_analytic_list.append(models.InstrumentAnalytic(
                instrument, idx * 100.0))

        # add prices from the aggregation
        response = self.client.set_analytics(scope,
                                             self.effective_date.year,
                                             self.effective_date.month,
                                             self.effective_date.day,
                                             instrument_analytic_list)

        # Create the aggregation request. Note we are filtering out the start cash.
        # If not, there will be an extra instrument, with end value £1
        aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope, "default"),
                                                        metrics=[models.AggregateSpec(self.GROUPBY_KEY, "Value"),
                                                                 models.AggregateSpec(self.AGGREGATION_KEY, "Proportion"),
                                                                 models.AggregateSpec(self.AGGREGATION_KEY, "Sum")],
                                                        group_by=[self.GROUPBY_KEY],
                                                        effective_at=self.effective_date,
                                                        filters=[models.PropertyFilter(
                                                            left=self.GROUPBY_KEY,
                                                            operator='NotEquals',
                                                            right='<Unknown>',
                                                            right_operand_type='Absolute')])

        # do the aggregation
        aggregation_response = self.client.get_aggregation_by_portfolio(scope, portfolio_id, aggregation_request)

        # sort by instrument name
        validate_results = sorted(aggregation_response.data, key=lambda k: k[self.GROUPBY_KEY])

        # print out the results
        for item in validate_results:
            print("\t{}\t{}\t{}".format(item[self.GROUPBY_KEY], item["Proportion(" + self.AGGREGATION_KEY + ")"],
                                        item["Sum(" + self.AGGREGATION_KEY + ")"]))

        return validate_results


if __name__ == '__main__':
    unittest.main()
