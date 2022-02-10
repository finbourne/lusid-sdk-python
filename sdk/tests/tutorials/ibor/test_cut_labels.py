import unittest
import uuid
from datetime import date, timedelta

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class CutLabels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

        cls.cut_labels = lusid.CutLabelDefinitionsApi(api_client)

    @lusid_feature("F16-3")
    def test_cut_labels(self):
        def get_guid():
            return str(uuid.uuid4())[:4]

        # define function to format cut labels
        def cut_label_formatter(date, cut_label_code):
            return str(date) + "N" + cut_label_code

        # Create cut labels
        code = {}

        def create_cut_label(hours, minutes, display_name, description, time_zone, code_dict):
            # Create the time for the cut label
            time = models.CutLocalTime(hours=hours, minutes=minutes)

            # Define the parameters of the cut label in a request
            request = models.CutLabelDefinition(
                code=display_name + "-" + get_guid(),
                description=description,
                display_name=display_name,
                cut_local_time=time,
                time_zone=time_zone)

            # Add the codes of our cut labels to our dictionary
            code_dict[request.display_name] = request.code

            # Send the request to LUSID to create the cut label
            result = self.cut_labels.create_cut_label_definition(
                create_cut_label_definition_request=request)

            # Check that result gives same details as input
            self.assertEqual(result.display_name, display_name)
            self.assertEqual(result.description, description)
            self.assertEqual(result.cut_local_time, time)
            self.assertEqual(result.time_zone, time_zone)

        # Create cut labels for different time zones
        create_cut_label(hours=9, minutes=0, display_name="LondonOpen", description="London Opening Time, 9am in UK",
                         time_zone="GB", code_dict=code)
        create_cut_label(hours=17, minutes=0, display_name="LondonClose", description="London Closing Time, 5pm in UK",
                         time_zone="GB", code_dict=code)
        create_cut_label(hours=9, minutes=0, display_name="SingaporeOpen", description="", time_zone="Singapore",
                         code_dict=code)
        create_cut_label(hours=17, minutes=0, display_name="SingaporeClose", description="", time_zone="Singapore",
                         code_dict=code)
        create_cut_label(hours=9, minutes=0, display_name="NYOpen", description="", time_zone="America/New_York",
                         code_dict=code)
        create_cut_label(hours=17, minutes=0, display_name="NYClose", description="", time_zone="America/New_York",
                         code_dict=code)

        ## Create portfolio
        scope = 'cut_labels_demo'
        portfolio_code = self.test_data_utilities.create_transaction_portfolio(scope)

        ## Get the instrument identifiers
        instrument1 = self.instrument_ids[0]
        instrument2 = self.instrument_ids[1]
        instrument3 = self.instrument_ids[2]

        currency = "GBP"

        # set a currency LUID, as the call to GetHoldings returns the LUID not the identifier we are about to create
        currency_luid = "CCY_{}".format(currency)

        ## Set initial holdings for each instrument from LondonOpen 5 days ago 
        initial_holdings_cut_label = cut_label_formatter(date.today() - timedelta(days=5), code["LondonOpen"])
        initial_holdings = [
            # cash balance
            self.test_data_utilities.build_cash_funds_in_adjust_holdings_request(currency=currency, units=100000.0),
            # instrument 1
            self.test_data_utilities.build_adjust_holdings_request(instrument_id=instrument1,
                                                                   units=100.0,
                                                                   price=101.0,
                                                                   currency=currency,
                                                                   trade_date=None
                                                                   ),
            # instrument 2
            self.test_data_utilities.build_adjust_holdings_request(instrument_id=instrument2,
                                                                   units=100.0,
                                                                   price=102.0,
                                                                   currency=currency,
                                                                   trade_date=None
                                                                   ),
            # instrument 3
            self.test_data_utilities.build_adjust_holdings_request(instrument_id=instrument3,
                                                                   units=100.0,
                                                                   price=99.0,
                                                                   currency=currency,
                                                                   trade_date=None
                                                                   )
        ]
        # add initial holdings to our portfolio from LondonOpen 5 days ago
        self.transaction_portfolios_api.set_holdings(scope=scope,
                                                     code=portfolio_code,
                                                     adjust_holding_request=initial_holdings,
                                                     effective_at=initial_holdings_cut_label)

        ## Check initial holdings
        # get holdings at LondonOpen today, before transactions occur
        get_holdings_cut_label = cut_label_formatter(date.today(), code["LondonOpen"])
        holdings = self.transaction_portfolios_api.get_holdings(scope=scope,
                                                                code=portfolio_code,
                                                                effective_at=get_holdings_cut_label)
        # check that holdings are as expected before transactions occur for each instrument
        holdings.values.sort(key=lambda i: i.instrument_uid)
        self.assertEqual(len(holdings.values), 4)
        self.test_data_utilities.test.assert_cash_holdings(holdings=holdings,
                                                           index=0,
                                                           instrument_id=currency_luid,
                                                           units=100000.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=1,
                                                      instrument_id=instrument1,
                                                      units=100.0,
                                                      cost_amount=10100.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=2,
                                                      instrument_id=instrument2,
                                                      units=100.0,
                                                      cost_amount=10200.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=3,
                                                      instrument_id=instrument3,
                                                      units=100.0,
                                                      cost_amount=9900.0)

        ## Add transactions at different times in different time zones during the day with cut labels
        transaction_1_cut_label = cut_label_formatter(date.today(), code["LondonOpen"])
        transaction_2_cut_label = cut_label_formatter(date.today(), code["SingaporeClose"])
        transaction_3_cut_label = cut_label_formatter(date.today(), code["NYOpen"])
        transaction_4_cut_label = cut_label_formatter(date.today(), code["NYClose"])
        transactions = [
            self.test_data_utilities.build_transaction_request(instrument_id=instrument1,
                                                               units=100.0,
                                                               price=100.0,
                                                               currency=currency,
                                                               trade_date=transaction_1_cut_label,
                                                               transaction_type="Buy"),
            self.test_data_utilities.build_transaction_request(instrument_id=instrument2,
                                                               units=100.0,
                                                               price=100.0,
                                                               currency=currency,
                                                               trade_date=transaction_2_cut_label,
                                                               transaction_type="Buy"),
            self.test_data_utilities.build_transaction_request(instrument_id=instrument3,
                                                               units=100.0,
                                                               price=100.0,
                                                               currency=currency,
                                                               trade_date=transaction_3_cut_label,
                                                               transaction_type="Buy"),
            self.test_data_utilities.build_transaction_request(instrument_id=instrument1,
                                                               units=100.0,
                                                               price=100.0,
                                                               currency=currency,
                                                               trade_date=transaction_4_cut_label,
                                                               transaction_type="Buy")
        ]
        # Add transactions to the portfolio
        self.transaction_portfolios_api.upsert_transactions(scope=scope,
                                                            code=portfolio_code,
                                                            transaction_request=transactions)

        ## Retrieve holdings at LondonClose today (5pm local time)
        # This will mean that the 4th transaction will not be included, demonstrating how cut labels work across time zones
        get_holdings_cut_label = cut_label_formatter(date.today(), code["LondonClose"])
        holdings = self.transaction_portfolios_api.get_holdings(scope=scope,
                                                                code=portfolio_code,
                                                                effective_at=get_holdings_cut_label)

        # check that holdings are as expected after transactions for each instrument
        holdings.values.sort(key=lambda i: i.instrument_uid)
        self.assertEqual(len(holdings.values), 4)
        self.test_data_utilities.test.assert_cash_holdings(holdings=holdings,
                                                           index=0,
                                                           instrument_id=currency_luid,
                                                           units=70000.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=1,
                                                      instrument_id=instrument1,
                                                      units=200.0,
                                                      cost_amount=20100.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=2,
                                                      instrument_id=instrument2,
                                                      units=200.0,
                                                      cost_amount=20200.0)
        self.test_data_utilities.test.assert_holdings(holdings=holdings,
                                                      index=3,
                                                      instrument_id=instrument3,
                                                      units=200.0,
                                                      cost_amount=19900.0)
