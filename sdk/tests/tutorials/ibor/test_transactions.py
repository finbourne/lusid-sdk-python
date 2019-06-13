import unittest
from datetime import datetime

import pytz
import uuid

import lusid
import lusid.models as models

from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.instrument_loader import InstrumentLoader
from utilities.test_data_utilities import TestDataUtilities
from utilities.credentials_source import CredentialsSource


class Transactions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    def test_load_listed_instrument_transaction(self):
        # create the portfolio
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        trade_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        #   details of the transaction to be added
        transaction = models.TransactionRequest(

            # unique transaction id
            transaction_id=str(uuid.uuid4()),

            # transaction type, configured during system setup
            type="Buy",
            instrument_identifiers={TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]},
            transaction_date=trade_date,
            settlement_date=trade_date,
            units=100,
            transaction_price=models.TransactionPrice(12.3),
            total_consideration=models.CurrencyAndAmount(1230, "GBP"),
            source="Client"
        )

        # add the transaction
        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transactions=[transaction])

        # get the transaction
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 1)
        self.assertEqual(transactions.values[0].transaction_id, transaction.transaction_id)

    def test_load_cash_transaction(self):
        # create the portfolio
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        trade_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        #   details of the transaction to be added
        transaction = models.TransactionRequest(

            # unique transaction id
            transaction_id=str(uuid.uuid4()),

            # transaction type, configured during system setup
            type="FundsIn",

            # Cash instruments are identified using CCY_ followed by the ISO currency codes.
            # Cash instruments do not need to be created before use
            instrument_identifiers={TestDataUtilities.lusid_cash_identifier: "GBP"},

            transaction_date=trade_date,
            settlement_date=trade_date,
            transaction_price=models.TransactionPrice(0.0),
            units=0,
            total_consideration=models.CurrencyAndAmount(0, "GBP"),
            source="Client"
        )

        # add the transaction
        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transactions=[transaction])

        # get the transaction
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 1)
        self.assertEqual(transactions.values[0].transaction_id, transaction.transaction_id)

    def test_load_otc_instrument_transaction(self):
        # create the portfolio
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        trade_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        swap_definition = models.InstrumentDefinition(
            name="10mm 5Y Fixed",
            identifiers={
                "ClientInternal": models.InstrumentIdValue(value="SW-1")
            },
            definition=models.InstrumentEconomicDefinition(
                instrument_format="CustomFormat",
                content="<customFormat>upload in custom xml or JSON format</customFormat>"))

        # create the swap
        swap_response = self.instruments_api.upsert_instruments(requests={
            "request": swap_definition
        })

        # get the LUID for the created instrument
        swap_id = list(swap_response.values.values())[0].lusid_instrument_id

        #   details of the transaction to be added
        transaction = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="Buy",
            instrument_identifiers={TestDataUtilities.lusid_luid_identifier: swap_id},
            transaction_date=trade_date,
            settlement_date=trade_date,
            units=1,
            transaction_price=models.TransactionPrice(0.0),
            total_consideration=models.CurrencyAndAmount(0.0, "GBP"),
            source="Client"
        )

        # add the transaction
        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transactions=[transaction])

        # get the transaction
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 1)
        self.assertEqual(transactions.values[0].transaction_id, transaction.transaction_id)
