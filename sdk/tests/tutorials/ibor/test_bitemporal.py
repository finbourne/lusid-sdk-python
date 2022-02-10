import unittest
from datetime import datetime
from time import sleep

import pytz

import lusid
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Bitemporal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

        instruments_api = lusid.InstrumentsApi(api_client)
        instrument_loader = InstrumentLoader(instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    def print_transactions(self, as_at, transactions):
        print("transactions at: {}".format(as_at))

        for transaction in transactions:
            print("{}\t{}\t{}\t{}\t{}".format(transaction.instrument_uid,
                                              transaction.transaction_date,
                                              transaction.units,
                                              transaction.transaction_price.price,
                                              transaction.total_consideration.amount))

    @lusid_feature("F2-3")
    def test_apply_bitemporal_portfolio_change(self):
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        initial_transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=100,
                                                               price=101,
                                                               currency="GBP",
                                                               trade_date=datetime(2018, 1, 1, tzinfo=pytz.utc),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[1],
                                                               units=100,
                                                               price=102,
                                                               currency="GBP",
                                                               trade_date=datetime(2018, 1, 2, tzinfo=pytz.utc),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[2],
                                                               units=100,
                                                               price=103,
                                                               currency="GBP",
                                                               trade_date=datetime(2018, 1, 3, tzinfo=pytz.utc),
                                                               transaction_type="StockIn")
        ]

        # add the initial batch of transactions
        inital_result = self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_code,
                                                                            transaction_request=initial_transactions)

        as_at_1 = inital_result.version.as_at_date
        sleep(0.5)

        # add another trade for 2018-1-8
        new_trade = self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[3],
                                                                       units=100,
                                                                       price=104,
                                                                       currency="GBP",
                                                                       trade_date=datetime(2018, 1, 8, tzinfo=pytz.utc),
                                                                       transaction_type="StockIn")
        added_result = self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                           code=portfolio_code,
                                                                           transaction_request=[new_trade])
        as_at_2 = added_result.version.as_at_date
        sleep(0.5)

        # add back dated trade for 2018-1-5
        backdated_trade = self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[4],
                                                                             units=100,
                                                                             price=105,
                                                                             currency="GBP",
                                                                             trade_date=datetime(2018, 1, 5,
                                                                                                 tzinfo=pytz.utc),
                                                                             transaction_type="StockIn")

        added_result = self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                           code=portfolio_code,
                                                                           transaction_request=[backdated_trade])

        as_at_3 = added_result.version.as_at_date
        sleep(0.5)

        # list transactions at initial upload
        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code,
                                                                        as_at=as_at_1)
        self.assertEqual(len(transactions.values), 3)
        self.print_transactions(as_at_1, transactions.values)

        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code,
                                                                        as_at=as_at_2)

        self.assertEqual(len(transactions.values), 4)
        self.print_transactions(as_at_2, transactions.values)

        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code,
                                                                        as_at=as_at_3)

        self.assertEqual(len(transactions.values), 5)
        self.print_transactions(as_at_3, transactions.values)

        transactions = self.transaction_portfolios_api.get_transactions(scope=TestDataUtilities.tutorials_scope,
                                                                        code=portfolio_code)

        self.assertEqual(len(transactions.values), 5)
        self.print_transactions(datetime.now(), transactions.values)
