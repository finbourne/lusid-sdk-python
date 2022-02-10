import unittest
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Holdings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        cls.instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = cls.instrument_loader.load_instruments()

    @lusid_feature("F15-3")
    def test_get_holdings(self):
        # The currency of the cash and transactions
        currency = "GBP"

        # The dates for which transactions are added to the portfolio. All dates/times must be supplied in UTC
        day_t1 = datetime(2018, 1, 1, tzinfo=pytz.utc)
        day_tplus5 = datetime(2018, 1, 5, tzinfo=pytz.utc)
        day_tplus10 = datetime(2018, 1, 10, tzinfo=pytz.utc)

        # Create a portfolio
        portfolio_id = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        transactions = [
            # Starting cash position
            self.test_data_utilities.build_cash_fundsin_transaction_request(100000, currency, day_t1),

            # Initial transaction on day_t1
            self.test_data_utilities.build_transaction_request(self.instrument_ids[0], 100.0, 101.0, currency, day_t1,
                                                               "Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[1], 100.0, 102.0, currency, day_t1,
                                                               "Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[2], 100.0, 103.0, currency, day_t1,
                                                               "Buy"),

            # On T+5, add a transaction in another instrument and another to increase the amount of instrument 1
            self.test_data_utilities.build_transaction_request(self.instrument_ids[1], 100.0, 104.0, currency,
                                                               day_tplus5, "Buy"),
            self.test_data_utilities.build_transaction_request(self.instrument_ids[3], 100.0, 105.0, currency,
                                                               day_tplus5, "Buy"),
        ]

        # Upload the transactions to LUSID
        self.transaction_portfolios_api.upsert_transactions(TestDataUtilities.tutorials_scope, code=portfolio_id,
                                                            transaction_request=transactions)

        # Get the portfolio holdings on T+10
        holdings = self.transaction_portfolios_api.get_holdings(TestDataUtilities.tutorials_scope, portfolio_id,
                                                                effective_at=day_tplus10)

        # Ensure we have 5 holdings: 1 cash position and a position in 4 instruments that aggregates the 5 transactions
        self.assertEqual(len(holdings.values), 5, msg="Unexpected number of holdings")

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

    @lusid_feature("F15-1")
    def test_set_target_holdings(self):

        currency = "GBP"

        day1 = datetime(2018, 1, 1, tzinfo=pytz.utc)
        day2 = datetime(2018, 1, 5, tzinfo=pytz.utc)

        portfolio_code = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        instrument1 = self.instrument_ids[0]
        instrument2 = self.instrument_ids[1]
        instrument3 = self.instrument_ids[2]

        holdings_adjustments = [

            # cash balance
            models.AdjustHoldingRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_cash_identifier: currency
                },
                tax_lots=[
                    models.TargetTaxLotRequest(units=100000.0)
                ]),

            # instrument 1
            models.AdjustHoldingRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_luid_identifier: instrument1
                },
                tax_lots=[
                    models.TargetTaxLotRequest(units=100.0,
                                               price=101.0,
                                               cost=models.CurrencyAndAmount(amount=10100.0, currency=currency),
                                               portfolio_cost=10100.0,
                                               purchase_date=day1,
                                               settlement_date=day1)
                ]),

            # instrument 2
            models.AdjustHoldingRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_luid_identifier: instrument2
                },
                tax_lots=[
                    models.TargetTaxLotRequest(units=100.0,
                                               price=102.0,
                                               cost=models.CurrencyAndAmount(amount=10200.0, currency=currency),
                                               portfolio_cost=10200.0,
                                               purchase_date=day1,
                                               settlement_date=day1)
                ])
        ]

        # set the initial holdings on day 1
        self.transaction_portfolios_api.set_holdings(scope=TestDataUtilities.tutorials_scope,
                                                     code=portfolio_code,
                                                     adjust_holding_request=holdings_adjustments,
                                                     effective_at=day1)

        # add subsequent transactions on day 2
        transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=instrument1,
                                                               units=100.0,
                                                               price=104.0,
                                                               currency=currency,
                                                               trade_date=day2,
                                                               transaction_type="Buy"),
            self.test_data_utilities.build_transaction_request(instrument_id=instrument3,
                                                               units=100.0,
                                                               price=103.0,
                                                               currency=currency,
                                                               trade_date=day2,
                                                               transaction_type="Buy")
        ]

        self.transaction_portfolios_api.upsert_transactions(scope=TestDataUtilities.tutorials_scope,
                                                            code=portfolio_code,
                                                            transaction_request=transactions)

        # get the holdings for day 2
        holdings = self.transaction_portfolios_api.get_holdings(scope=TestDataUtilities.tutorials_scope,
                                                                code=portfolio_code,
                                                                effective_at=day2)

        # sort to put the cash instrument first
        holdings.values.sort(key=lambda i: i.instrument_uid)

        # cash balance + 3 holdings
        self.assertEqual(len(holdings.values), 4)

        # remaining cash balance which takes into account the purchase transactions on day 2

        # the call to GetHoldings returns the LUID not the identifier we created
        currency_luid = "CCY_{}".format(currency)

        # cash
        self.assertEqual(holdings.values[0].instrument_uid, currency_luid)
        self.assertEqual(holdings.values[0].units, 79300.0)

        # instrument 1 - initial holding + transaction on day 2
        self.assertEqual(holdings.values[1].instrument_uid, instrument1)
        self.assertEqual(holdings.values[1].units, 200.0)
        self.assertEqual(holdings.values[1].cost.amount, 20500.0)

        # instrument 2 - initial holding
        self.assertEqual(holdings.values[2].instrument_uid, instrument2)
        self.assertEqual(holdings.values[2].units, 100.0)
        self.assertEqual(holdings.values[2].cost.amount, 10200.0)

        # instrument 3 - transaction on day 2
        self.assertEqual(holdings.values[3].instrument_uid, instrument3)
        self.assertEqual(holdings.values[3].units, 100.0)
        self.assertEqual(holdings.values[3].cost.amount, 10300.0)



