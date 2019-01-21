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
from InstrumentLoader import InstrumentLoader


try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestTransactionsAPI(TestCase):
    client = None
    instrumentIds = []


    @classmethod
    def setUpClass(cls):

        cls.ISIN_PROPERTY_KEY = "Instrument/default/Isin"
        cls.SEDOL_PROPERTY_KEY = "Instrument/default/Sedol"
        cls.FIGI_SCHEME = "Figi"
        cls.CUSTOM_INTERNAL_SCHEME = "ClientInternal"
        cls.inst_loader = ""

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

        assert okta_response.status_code == 200

        # Retrieve our api token from the authentication response
        cls.api_token = {"access_token": okta_response.json()["access_token"]}

        # Initialise our API client using our token so that we can include it in all future requests
        credentials = BasicTokenAuthentication(cls.api_token)
        cls.client = lusid.LUSIDAPI(credentials, cls.api_url)

        # load the instruments using InstrumentLoader
        cls.inst_loader = InstrumentLoader()
        loader_response = cls.inst_loader.load_instruments(cls)

        assert len(loader_response.values) == 5

    def test_load_listed_instrument_transaction(self):

        uuid_gen = uuid.uuid4()
        scope = "finbourne"
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=effective_date)
        # create the portfolio
        portfolio_response = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio_response.id.code, request.code)

        portfolio_id = portfolio_response.id.code

        # create the transaction
        transaction_request = models.TransactionRequest(
                                    transaction_id=str(uuid.uuid4()),
                                    type="Buy",
                                    instrument_uid=
                                    self.inst_loader.instrument_response.values['correlationId1'].lusid_instrument_id,
                                    transaction_date=effective_date,
                                    settlement_date=effective_date,
                                    units=100.0,
                                    transaction_price=models.TransactionPrice(12.3),
                                    total_consideration=models.CurrencyAndAmount(100 * 12.3, "GBP"),
                                    source="Client")
        # add the trade
        upsert_response = self.client.upsert_transactions(scope, portfolio_id, [transaction_request])

        # get the trade again
        returned_transaction = self.client.get_transactions(scope, portfolio_id )
        assert returned_transaction.count == 1
        assert transaction_request.transaction_id == returned_transaction.values[0].transaction_id

    def test_zzload_cash_transactions(self):

        uuid_gen = uuid.uuid4()
        scope = "finbourne"
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=effective_date)
        # create the portfolio
        portfolio_response = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio_response.id.code, request.code)

        portfolio_id = portfolio_response.id.code

        # create the transaction
        # Cash instruments are identified using CCY_ followed by the ISO currency codes.
        # Cash instruments do not need to be created before use
        transaction_request = models.TransactionRequest(
                                    transaction_id=str(uuid.uuid4()),
                                    type="FundsIn",
                                    instrument_uid="CCY_GBP",
                                    transaction_date=effective_date,
                                    settlement_date=effective_date,
                                    units=100.0,
                                    transaction_price=models.TransactionPrice(0.0),    # this is not included in java version
                                    total_consideration=models.CurrencyAndAmount(0.0, "GBP"),
                                    source="Client")

        # add the trade
        upsert_response = self.client.upsert_transactions(scope, portfolio_id, [transaction_request])

        # get the trade again
        returned_transaction = self.client.get_transactions(scope, portfolio_id)
        assert returned_transaction.count == 1
        assert transaction_request.transaction_id == returned_transaction.values[0].transaction_id

    def test_load_otc_instrument_transaction(self):
        uuid_gen = uuid.uuid4()
        scope = "finbourne"
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=effective_date)
        # create the portfolio
        portfolio_response = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio_response.id.code, request.code)

        portfolio_id = portfolio_response.id.code

        # create a swap otc transaction
        swap_definition = models.InstrumentDefinition(name="10mm 5Y Fixed",
                                                      identifiers={"ClientInternal": "SW-1"},
                                                      definition=models.InstrumentEconomicDefinition(
                                                          instrument_format="CustomFormat",
                                                          content=
                                                          "<customFormat>upload in custom xml or JSON format</customFormat>"
                                                      ))
        # upsert the swap
        upsert_response = self.client.upsert_instruments({"request": swap_definition})
        # return the swap lusid Id
        swap_id = list(upsert_response.values.values())[0].lusid_instrument_id

        # create the transaction
        transaction_request = models.TransactionRequest(
                                                        transaction_id=str(uuid.uuid4()),
                                                        type="Buy",
                                                        instrument_uid=swap_id,
                                                        transaction_date=effective_date,
                                                        settlement_date=effective_date,
                                                        units=1.0,
                                                        transaction_price=models.TransactionPrice(0),
                                                        total_consideration=models.CurrencyAndAmount(0, "GBP"),
                                                        source="Client")

        # add the trade
        upsert_response = self.client.upsert_transactions(scope, portfolio_id, [transaction_request])

        # get the trade again
        returned_transaction = self.client.get_transactions(scope, portfolio_id)

        assert returned_transaction.count == 1

        swap_transaction = returned_transaction.values[0]

        assert transaction_request.transaction_id == swap_transaction.transaction_id
        assert swap_id == swap_transaction.instrument_uid

    @classmethod
    def tearDownClass(cls):
        response = cls.inst_loader.tearDownClass(cls)

if __name__ == '__main__':
    unittest.main()

