import unittest
from datetime import datetime, timedelta

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Reconciliation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.reconciliations_api = lusid.ReconciliationsApi(api_client)

        instruments_api = lusid.InstrumentsApi(api_client)
        instrument_loader = InstrumentLoader(instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    @lusid_feature("F20-1")
    def test_reconcile_portfolio(self):
        # create the portfolio
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        today = datetime.now().astimezone(tz=pytz.utc)
        yesterday = today - timedelta(1)

        # create transactions for yesterday
        yesterdays_transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=1000.0,
                                                               price=100.0,
                                                               currency="GBP",
                                                               trade_date=yesterday + timedelta(hours=8),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=2300.0,
                                                               price=101.0,
                                                               currency="GBP",
                                                               trade_date=yesterday + timedelta(hours=12),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[1],
                                                               units=-1000.0,
                                                               price=102.0,
                                                               currency="GBP",
                                                               trade_date=yesterday + timedelta(hours=9),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[2],
                                                               units=1200.0,
                                                               price=103.0,
                                                               currency="GBP",
                                                               trade_date=yesterday + timedelta(hours=16),
                                                               transaction_type="StockIn"),
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[3],
                                                               units=2000.0,
                                                               price=103.0,
                                                               currency="GBP",
                                                               trade_date=yesterday + timedelta(hours=9),
                                                               transaction_type="StockIn"),
        ]

        # add the transactions to LUSID
        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transaction_request=yesterdays_transactions)

        # transactions for today
        todays_transactions = [

            # net long 300
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=-3000.0,
                                                               price=101.78,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=8),
                                                               transaction_type="StockIn"),

            # net long 1800
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[0],
                                                               units=1500.0,
                                                               price=101.78,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=12),
                                                               transaction_type="StockIn"),

            # flat
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[1],
                                                               units=1000.0,
                                                               price=102.0,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=12),
                                                               transaction_type="StockIn"),

            # net long 2400
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[2],
                                                               units=1200.0,
                                                               price=103.0,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=16),
                                                               transaction_type="StockIn"),

            # net long 3000
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[3],
                                                               units=1000.0,
                                                               price=103.0,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=9),
                                                               transaction_type="StockIn"),

            # net long 5000
            self.test_data_utilities.build_transaction_request(instrument_id=self.instrument_ids[3],
                                                               units=2000.0,
                                                               price=103.0,
                                                               currency="GBP",
                                                               trade_date=today + timedelta(hours=20),
                                                               transaction_type="StockIn"),
        ]

        # add the transactions to LUSID
        transactions_response = self.transaction_portfolios_api.upsert_transactions(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            transaction_request=todays_transactions)

        # get the time of the last update
        last_as_at = transactions_response.version.as_at_date

        # We now have the portfolio with 2 days worth of transactions, going to reconcile from T-1 20:00 to now,
        # this should reflect breaks for each instrument equal to the transactions from yesterday till 20:00 today
        reconciliation_request = models.PortfoliosReconciliationRequest(
            left=models.PortfolioReconciliationRequest(
                portfolio_id=models.ResourceId(scope=TestDataUtilities.tutorials_scope, code=portfolio_code),
                effective_at=yesterday + timedelta(hours=20),
                as_at=last_as_at
            ),
            right=models.PortfolioReconciliationRequest(
                portfolio_id=models.ResourceId(scope=TestDataUtilities.tutorials_scope, code=portfolio_code),
                effective_at=today + timedelta(hours=16),
                as_at=last_as_at
            ),
            instrument_property_keys=[TestDataUtilities.lusid_luid_identifier]
        )

        breaks = self.reconciliations_api.reconcile_holdings(portfolios_reconciliation_request=reconciliation_request)

        for rec_break in breaks.values:
            print("{}\t{}\t{}".format(rec_break.instrument_uid, rec_break.difference_units,
                                      rec_break.difference_cost.amount))

        rec_map = {b.instrument_uid: b for b in breaks.values}

        self.assertEqual(-1500, rec_map[self.instrument_ids[0]].difference_units)
        self.assertEqual(1000, rec_map[self.instrument_ids[1]].difference_units)
        self.assertEqual(1200, rec_map[self.instrument_ids[2]].difference_units)
        self.assertEqual(1000, rec_map[self.instrument_ids[3]].difference_units)

