import unittest
import uuid
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Transactions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    @lusid_feature("F13-9")
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
                                                            transaction_request=[transaction])

        # get the transaction
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 1)
        self.assertEqual(transactions.values[0].transaction_id, transaction.transaction_id)

    @lusid_feature("F13-2")
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
                                                            transaction_request=[transaction])

        # get the transaction
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 1)
        self.assertEqual(transactions.values[0].transaction_id, transaction.transaction_id)

    @lusid_feature("F13-6")
    def test_cancel_transactions(self):
        # set effective date
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # create portfolio code
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        # Upsert transactions
        transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=100,
                                                               price=101,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[1],
                                                               units=100,
                                                               price=102,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[2],
                                                               units=100,
                                                               price=103,
                                                               currency="GBP",
                                                               trade_date=effective_date,
                                                               transaction_type="StockIn")
        ]

        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transaction_request=transactions)

        # get transactions
        transaction_ids = []
        existing_transactions = self.transaction_portfolios_api.get_transactions(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code)

        for i in range(len(existing_transactions.values)):
            transaction_ids.append(existing_transactions.values[i].transaction_id)

        # cancel transactions
        self.transaction_portfolios_api.cancel_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transaction_ids=transaction_ids)

        # verify portfolio is now empty
        new_transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_code)
        self.assertEqual(len(new_transactions.values), 0)
