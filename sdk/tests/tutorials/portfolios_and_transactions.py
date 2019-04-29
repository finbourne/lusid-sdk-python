import unittest
from datetime import datetime

import pytz
import uuid

import lusid
from api_client_builder import ApiClientBuilder
from instrument_loader import InstrumentLoader
from test_data_utilities import TestDataUtilities


class PortfoliosAndTransactions(unittest.TestCase):
    tutorial_scope = "Testdemo"

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build("secrets.json")

        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        cls.instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = cls.instrument_loader.load_instruments()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.instrument_loader.delete_instruments()

    def test_list_scopes(self):
        # Get the list of scopes across all entities
        scopes = self.scopes_api.list_scopes()

        self.assertGreater(scopes.count, 0)

    def test_list_portfolios(self):
        # This defines the scope that the portfolios will be retrieved from
        scope = self.tutorial_scope + str(uuid.uuid4())

        for i in range(10):
            self.test_data_utilities.create_transaction_portfolio(scope)

        # Retrieve the list of portfolios
        portfolios = self.portfolios_api.list_portfolios_for_scope(scope)

        self.assertEqual(portfolios.count, 10)

    def test_get_holdings(self):
        # The currency of the cash and transactions
        currency = "GBP"

        # The dates for which transactions are added to the portfolio. All dates/times must be supplied in UTC
        dayT1 = datetime(2018, 1, 1, tzinfo=pytz.utc)
        dayTPlus5 = datetime(2018, 1, 5, tzinfo=pytz.utc)
        dayTPlus10 = datetime(2018, 1, 10, tzinfo=pytz.utc)

        # Create a portfolio
        portfolio_id = self.test_data_utilities.create_transaction_portfolio(self.tutorial_scope)

        transactions = [
            # Starting cash position
            self.test_data_utilities.build_cash_fundsin_transaction_request(100000, currency, dayT1),

            # Initial transaction on dayT1
            self.test_data_utilities.build_transaction_request(self.instrument_ids[0], 100.0, 101.0, currency, dayT1, "Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[1], 100.0, 102.0, currency, dayT1, "Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[2], 100.0, 103.0, currency, dayT1, "Buy"),

            # On T+5, add a transaction in another instrument and another to increase the amount of instrument 1
            self.test_data_utilities.build_transaction_request(self.instrument_ids[1], 100.0, 104.0, currency, dayTPlus5,"Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[3], 100.0, 105.0, currency, dayTPlus5, "Buy"),
        ]

        # Upload the transactions to LUSID
        self.transaction_portfolios_api.upsert_transactions(self.tutorial_scope, code=portfolio_id, transactions=transactions)

        # Get the portfolio holdings on T+10
        holdings = self.transaction_portfolios_api.get_holdings(self.tutorial_scope, portfolio_id, effective_at=dayTPlus10)

        # Ensure we have 5 holdings: 1 cash position and a position in 4 instruments that aggregates the 5 transactions
        self.assertEqual(holdings.count, 5, msg="Unexpected number of holdings")

        holdings.values.sort(key=lambda x: x.instrument_uid)

        # Check the cash balance
        self.assertEqual(holdings.values[0].instrument_uid, "CCY_{}".format(currency))

        # Validate the holdings
        self.assertEqual(holdings.values[0].holding_type, "B")

        self.assertEqual(holdings.values[1].holding_type, "P", msg="Incorrect holding type")
        self.assertEqual(holdings.values[1].instrument_uid, self.instrument_ids[0], msg="Incorrect instrument id")
        self.assertEqual(holdings.values[1].units, 100.0, msg="Incorrect units")
        self.assertEqual(holdings.values[1].cost.amount, 10100.0, msg="Incorrect amount")

        self.assertEqual(holdings.values[2].holding_type, "P", msg="Incorrect holding type")
        self.assertEqual(holdings.values[2].instrument_uid, self.instrument_ids[1], msg="Incorrect instrument id")
        self.assertEqual(holdings.values[2].units, 200.0, msg="Incorrect units")
        self.assertEqual(holdings.values[2].cost.amount, 20600.0, msg="Incorrect amount")

        self.assertEqual(holdings.values[3].holding_type, "P", msg="Incorrect holding type")
        self.assertEqual(holdings.values[3].instrument_uid, self.instrument_ids[2], msg="Incorrect instrument id")
        self.assertEqual(holdings.values[3].units, 100.0, msg="Incorrect units")
        self.assertEqual(holdings.values[3].cost.amount, 10300.0, msg="Incorrect amount")

        self.assertEqual(holdings.values[4].holding_type, "P", msg="Incorrect holding type")
        self.assertEqual(holdings.values[4].instrument_uid, self.instrument_ids[3], msg="Incorrect instrument id")
        self.assertEqual(holdings.values[4].units, 100.0, msg="Incorrect units")
        self.assertEqual(holdings.values[4].cost.amount, 10500.0, msg="Incorrect amount")
