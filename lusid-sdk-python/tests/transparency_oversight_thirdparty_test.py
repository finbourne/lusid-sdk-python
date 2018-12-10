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
from datetime import datetime, timedelta
from finbournetest import TestFinbourneApi

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url

class transparencyOversightThirdParty(TestFinbourneApi):

    def import_data(self):
        '''
        We are an asset manager who has outsourced our fund accounting. We have multiple clients, each with multiple
        portfolios containing different investment strategies and priorities.

        Unfortunately we have recently been seeing significant outflows from our fund into passive asset management.
        To halt these flows we are feeling the pressure to drive superior performance and reduce costs.

        Outsourcing our fund accounting was a big part of this plan, however there have been a large number of
        significant discrepancies between our records and those of the fund accountant. Thus we have had to set up an
        internal 'shadow' team to reconcile the differences between our records and those of the fund accountant. The
        cost of running this team almost completely negates the cost saving of outsourcing our fund accounting.
        In addition, there have been many times were we have had to accept the records of the fund accountant as being
        correct which has lead to a number of investment strategies being much less profitable then our calculations
        initially suggested.

        Ideally we would take our fund accounting back in house or find another provider. However as they have been
        storing all of our historical data in their system we are locked in with them.

        We desperately need a solution that allows us to easily & automatically identify & reconcile the discrepancies
        between our records and the fund accountant.
        '''

        '''
        In LUSID we can create separate environments for our records and those of the fund accountant using Scopes. 
        A Scope is a container which acts as a separate namespace. This allows us to have a portfolio with the same code 
        in different scopes without having to worry about collisions.
        '''

        # Create a unique id for our scopes
        internal_scope_id = uuid.uuid4()
        fund_accountant_scope_id = uuid.uuid4()
        # Using the ids create a unique code for each scope, this is what identifies the scope
        self.internal_scope_code = 'internal-{}'.format(internal_scope_id)
        self.fund_accountant_scope_code = 'fund-accountant-{}'.format(fund_accountant_scope_id)

        '''
        We have three clients each with a varying number of portfolios. In LUSID we can use Portfolio Groups to group
        the different portfolios of each of our clients together. Let us create a unique identifier for each client's
        group of portfolios and then we can build our portfolio codes using this id. 
        '''
        # Also create a code for our portfolio, we will re-use the same code in each scope
        self.client_1_portfolio_group_id = uuid.uuid4()
        self.client_2_portfolio_group_id = uuid.uuid4()
        self.client_3_portfolio_group_id = uuid.uuid4()

        self.client_portfolios = {
            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id),
                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id),
                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id)
            ],
            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id),
                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id),
                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id),
                'client-{}-strategy-international'.format(self.client_2_portfolio_group_id),
                'client-{}-strategy-usgovt'.format(self.client_2_portfolio_group_id)
            ],
            'client-{}-portfolios'.format(self.client_3_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id),
                'client-{}-strategy-fixedincome'.format(self.client_3_portfolio_group_id)
            ]
        }

    def create_portfolios(self):
        '''
        Let us create our portfolios and portfolio groups in both our internal and fund accountant scopes.

        Note that we can only create one portfolio at a time. We will create our portfolios for each client and then
        we will create the portfolio group that holds them
        '''

        # Iterate over our portfolio groups selecting the name of the group and the list of portfolios
        for portfolio_group_code, portfolio_group in self.client_portfolios.items():
            # Loop over our list of portfolios selecting the portfolio code
            for portfolio_code in portfolio_group:
                # Create the request to add our portfolio
                portfolio_request = models.CreateTransactionPortfolioRequest(display_name=portfolio_code,
                                                                             code=portfolio_code,
                                                                             base_currency='GBP',
                                                                             description=portfolio_code)
                # Create our portfolio in the internal scope
                portfolio_internal = self.client.create_portfolio(scope=self.internal_scope_code,
                                                                  create_request=portfolio_request)
                # Create our portfolio in the fund accountant scope
                portfolio_fund_accountant = self.client.create_portfolio(scope=self.fund_accountant_scope_code,
                                                                         create_request=portfolio_request)

                # Tests - Ensure that the portfolios were created successfully with the correct details
                self.portfolio_creation_tests(portfolio_internal, portfolio_request, self.internal_scope_code)
                self.portfolio_creation_tests(portfolio_fund_accountant, portfolio_request, self.fund_accountant_scope_code)

            '''
            To create our groups we need the scope and code of each of our portfolios. In LUSID these are contained
            inside a ResourceId object. We use ResourceId objects anytime we need to specify the scope and code of
            an object such as a portfolio. 
            
            This means that unlike when we created the portfolios we need two separate requests to create our groups. 
            One for each scope. 
            '''
            # Create the lists of resourceids for each scope, these are the portfolios to add to the group
            portfolio_resourceids_internal = [models.ResourceId(scope=self.internal_scope_code, code=portfolio_code) for portfolio_code in portfolio_group]
            portfolio_resourceids_fund_accountant = [models.ResourceId(scope=self.fund_accountant_scope_code, code=portfolio_code) for portfolio_code in portfolio_group]

            # Create our portfolio group requests, note the only difference is in which portfolios we use
            portfolio_group_request_internal = models.CreatePortfolioGroupRequest(id=portfolio_group_code,
                                                                                  display_name=portfolio_group_code,
                                                                                  values=portfolio_resourceids_internal,
                                                                                  description=portfolio_group_code)

            portfolio_group_request_fund_accountant = models.CreatePortfolioGroupRequest(id=portfolio_group_code,
                                                                                         display_name=portfolio_group_code,
                                                                                         values=portfolio_resourceids_fund_accountant,
                                                                                         description=portfolio_group_code)

            # Create our portfolio groups, note the different scope for each request
            portfolio_group_internal = self.client.create_portfolio_group(scope=self.internal_scope_code,
                                                                          request=portfolio_group_request_internal)

            portfolio_group_fund_accountant = self.client.create_portfolio_group(scope=self.fund_accountant_scope_code,
                                                                                 request=portfolio_group_request_fund_accountant)

            # Tests - Ensure that we have successfully created the portfolio groups
            self.portfolio_group_creation_tests(portfolio_group_internal, portfolio_group_request_internal, self.internal_scope_code)
            self.portfolio_group_creation_tests(portfolio_group_fund_accountant, portfolio_group_request_fund_accountant, self.fund_accountant_scope_code)

    def create_entitlements(self):
        pass

    def create_holdings(self):
        '''
        Now that we have our portfolios and groups set up for our clients we can add in their current holdings. We will
        with having the internal scope and the fund account scope completely in sync with exactly the same
        holdings. This will be our initial state.
        '''

        '''
        Before we can set our holdings we first need to upsert our instrument into LUSID. We use the upsert method which
        will insert a new record if it does not exist and update the existing record if it does exist. This allows us
        to add instruments more simply than checking if an instrument exists before we insert it. 
        
        Below we have our universe of instruments which all our holdings are made up of. Using LUSID this universe
        can be pre-populated in advance so that we don't have to keep adding new instruments when we make a trade or
        update a holding. 
        
        Here we can upsert our instruments individually or in a batch. Either way the request should be in the form of a
        dictionary with an arbitrary reference name for the instrument as the key and an UpsertInstrumentRequest object
        as the value.
        
        The UpsertInstrumentRequest requires a name for the instrument which is a string. In this case we will use the 
        same name as the arbitrary reference key.
        
        It also requires a dictionary containing at least one unique identifier for the asset. The key for this 
        dictionary is the name of the identifier, in this case we will use 'ClientInternal'. The value is a string which
        is the identifier. The allowed identifiers currently supported are:
        
            - ClientInternal
            - Figi
             
        '''

        self.instrument_universe = {
            'WPP_LondonStockEx_WPP': {
                'identifiers': {'ClientInternal': 'Isin-JE00B8KF9B49'},
                'currency': 'GBP'},

            'UKGiltTreasury_3.5_2045': {
                'identifiers': {'ClientInternal': 'Isin-GB00BN65R313'},
                'currency': 'GBP'},

            'UKGiltTreasury_2.0_2025': {
                'identifiers': {'ClientInternal': 'Isin-GB00BTHH2R79'},
                'currency': 'GBP'},

            'UKGiltTreasury_4.5_2034': {
                'identifiers': {'ClientInternal': 'Isin-GB00B52WS153'},
                'currency': 'GBP'},

            'UKGiltTreasury_3.75_2021': {
                'identifiers': {'ClientInternal': 'Isin-GB00B4RMG977'},
                'currency': 'GBP'},

            'Kingfisher_LondonStockEx_KGF': {
                'identifiers': {'ClientInternal': 'Isin-GB0033195214'},
                'currency': 'GBP'},

            'JustEat_LondonStockEx_JE': {
                'identifiers': {'ClientInternal': 'Isin-GB00BKX5CN86'},
                'currency': 'GBP'},

            'RELXGroup_LondonStockEx_REL': {
                'identifiers': {'ClientInternal': 'Isin-GB00B2B0DG97'},
                'currency': 'GBP'},

            'TESCO_LondonStockEx_TSCO': {
                'identifiers': {'ClientInternal': 'Isin-GB0008847096'},
                'currency': 'GBP'},

            'Whitebread_LondonStockEx_WTB': {
                'identifiers': {'ClientInternal': 'Isin-GB00B1KJJ408'},
                'currency': 'GBP'},

            'USTreasury_2.00_2021': {
                'identifiers': {'ClientInternal': 'Isin-US912828U816'},
                'currency': 'USD'},

            'USTreasury_6.875_2025': {
                'identifiers': {'ClientInternal': 'Isin-US912810EV62'},
                'currency': 'USD'},

            'BP_LondonStockEx_BP': {
                'identifiers': {'ClientInternal': 'Isin-GB0007980591'},
                'currency': 'GBP'},

            'MicroFocus_LondonStockEx_MCRO': {
                'identifiers': {'ClientInternal': 'Isin-GB00BD8YWM01'},
                'currency': 'GBP'},

            'Sage_LondonStockEx_SGE': {
                'identifiers': {'ClientInternal': 'Isin-GB00B8C3BL03'},
                'currency': 'GBP'},

            'BurfordCapital_LondonStockEx_BUR': {
                'identifiers': {'ClientInternal': 'Isin-GG00B4L84979'},
                'currency': 'GBP'},

            'EKFDiagnostics_LondonStockEx_EKF': {
                'identifiers': {'ClientInternal': 'Isin-GB0031509804'},
                'currency': 'GBP'},

            'Apple_Nasdaq_AAPL': {
                'identifiers': {'ClientInternal': 'Isin-US0378331005'},
                'currency': 'USD'},

            'Amazon_Nasdaq_AMZN': {
                'identifiers': {'ClientInternal': 'Isin-US0231351067'},
                'currency': 'USD'},

            'Glencore_LondonStockEx_GLEN': {
                'identifiers': {'ClientInternal': 'Isin-JE00B4T3BW64'},
                'currency': 'GBP'}
        }

        # Initialise our batch upsert request
        batch_upsert_request = {}
        # Using our instrument universe create our batch request
        for instrument_name, instrument in self.instrument_universe.items():
            batch_upsert_request[instrument_name] = models.UpsertInstrumentRequest(name=instrument_name,
                                                                                   identifiers=instrument['identifiers'])
        # Upsert our batch
        batch_upsert_response = self.client.upsert_instruments(requests=batch_upsert_request)

        # Tests - Confirm that the response is as expected
        self.instrument_upsert_tests(batch_upsert_response, batch_upsert_request)

        '''
        Every instrument that is created is in LUSID given a unique LUSID Instrument Id or LUID for short. This ID is 
        used for many methods and is how the API identifies an instrument. 

        Note that there is also a match feature that allows you to search for instruments using the identifiers that we 
        defined for each instrument, however it is preferred to use the LUID as this is guaranteed to be unique and 
        there is absolutely no chance of a collision. 

        We there want to add our newly created LUIDs to our initial holdings for future use
        '''

        # Loop over our recently upserted instruments
        for result, instrument in batch_upsert_response.values.items():
            # Loop over our instrument universe looking for the right match
            for instrument_name, new_instrument in self.instrument_universe.items():
                # If the identifiers match
                if new_instrument['identifiers']['ClientInternal'] == instrument.identifiers['ClientInternal']:
                    # Add our LUID as a new identifier so that we can use it in our calls later
                    new_instrument['identifiers']['LUID'] = instrument.lusid_instrument_id

        '''
        Now that we have our instruments added we can fill our initial holdings to model our live portfolio. 
        
        We will create the holdings data using a nested dictionary. Note that in reality this data would likely come
        from a historical report in a format such as CSV. In this case, a library such as Pandas can be used to 
        handle the data. 
        '''

        self.client_holdings = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id) : {
                    'WPP_LondonStockEx_WPP': {'quantity': 2956000, 'price': 8.7100},
                    'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                    'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                    'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126}
                },

                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id) : {
                    'MicroFocus_LondonStockEx_MCRO': {'quantity': 687994, 'price': 14.5350},
                    'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700}
                },

                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id) : {
                    'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                    'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700}
                },

            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id) : {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572}
                },

                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id) : {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140}
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id) : {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90}
                },

                'client-{}-strategy-international'.format(self.client_2_portfolio_group_id) : {
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'Apple_Nasdaq_AAPL': {'quantity': 504481, 'price': 168.49},
                    'Amazon_Nasdaq_AMZN': {'quantity': 38671, 'price': 1629.13}
                },

                'client-{}-strategy-usgovt'.format(self.client_2_portfolio_group_id) : {
                    'USTreasury_2.00_2021': {'quantity': 286006, 'price': 97.90},
                    'USTreasury_6.875_2025': {'quantity': 256986, 'price': 124.52}
                }

            },

            'client-{}-portfolios'.format(self.client_3_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id) : {
                    'Whitebread_LondonStockEx_WTB': {'quantity': 355318, 'price': 45.03},
                    'TESCO_LondonStockEx_TSCO': {'quantity': 2206441, 'price': 1.9715},
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 3312829, 'price': 2.276},
                    'UKGiltTreasury_3.75_2021': {'quantity': 128969, 'price': 108.126}
                },

                'client-{}-strategy-fixedincome'.format(self.client_3_portfolio_group_id) : {
                    'UKGiltTreasury_3.5_2045': {'quantity': 286388, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 581411, 'price': 106.637},
                    'USTreasury_2.00_2021': {'quantity': 796731, 'price': 97.9},
                    'USTreasury_6.875_2025': {'quantity': 277063, 'price': 124.52}
                }
            }
        }


        '''
        To set our holdings we use a list of AdjustHoldingRequest objects. We can create these from our holdings data
        above.
        
        The AdjustHoldingRequest object has a number of fields these are:
            - instrument_uid: This is the LUID of the instrument we want to adjust the holdings for
            - tax_lots: This is a list of tax lots. A tax lot being instruments purchased at different times and thus needing
                        different treatment for tax purposes. In this case we will use a single tax lot
                - units: This is the quantity of the instrument that we are holding
                - cost: This is the total cost of the instrument and the currency it is in
                    - amount: The total cost/value of the instrument, here we multiply the instrument's price by its
                              quantity to get the total amount
                    - currency: The currency that the instrument is in as a string, must be tk - what currencies are allowed??
                - portfolio_cost: This is the total cost of the instrument in the portfolio's currency
                - price: This is the price if the instrument tk - in what currency???? Is this in the portfolio currency?
        '''

        # Initialise our holding adjustments dictionary which will contain a list of adjustments for each portfolio in each portfolio group
        holding_adjustments = {}

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in self.client_holdings.items():
            # Create a key for our group to hold the portfolios
            holding_adjustments[portfolio_group_name] = {}
            # Iterate over our portfolios
            for portfolio_name, portfolio in portfolio_group.items():
                # Create a key and initialise a list to hold our adjustments for each portfolio
                holding_adjustments[portfolio_group_name][portfolio_name] = []
                # Iterate over the holdings in each portfolio
                for instrument_name, holding in portfolio.items():
                    # Create our adjust holdings request using our instrument universe to get the LUID identifier for the instrument
                    holding_adjustments[portfolio_group_name][portfolio_name].append(
                        models.AdjustHoldingRequest(instrument_uid=self.instrument_universe[instrument_name]['identifiers']['LUID'],
                                                    tax_lots=[
                                                        models.TargetTaxLotRequest(units=holding['quantity'],
                                                                                   cost=models.CurrencyAndAmount(
                                                                                       amount=holding['quantity'] *
                                                                                              holding['price'],
                                                                                       currency=self.instrument_universe[instrument_name]['currency']),
                                                                                   portfolio_cost=holding['quantity'] *
                                                                                                  holding['price'],
                                                                                   price=holding['price'])
                                                    ]
                                                    )
                    )

        '''
        Now that we have our holding adjustments we can set them on our portfolios. Using the set_holdings method
        we can only set holdings on one portfolio at a time. So we will have to iterate over our portfolios and create
        our holdings
        '''
        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in holding_adjustments.items():
            # Iterate over our portfolios
            for portfolio_name, portfolio_adjustments in portfolio_group.items():

                holdings_internal = self.client.set_holdings(scope=self.internal_scope_code,
                                                             code=portfolio_name,
                                                             effective_at=datetime.today().isoformat(),
                                                             holding_adjustments=portfolio_adjustments)

                holdings_fund_accountant = self.client.set_holdings(scope=self.fund_accountant_scope_code,
                                                                    code=portfolio_name,
                                                                    effective_at=datetime.today().isoformat(),
                                                                    holding_adjustments=portfolio_adjustments)

                # Tests to verify that the holdings are correct
                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings_internal,
                                           scope=self.internal_scope_code,
                                           code=portfolio_name,
                                           effective_at=datetime.today().isoformat())

                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings_fund_accountant,
                                           scope=self.fund_accountant_scope_code,
                                           code=portfolio_name,
                                           effective_at=datetime.today().isoformat())

    def add_daily_transactions(self):
        '''
        Now that we have our portfolios populated with their holdings we are going to simulate a day of trading.

        We have some exciting new strategies to implement that involve

        1)
        2)
        3)
        4)
        5)
        6)
        7)

        These trades are added to our internal scope as soon as they are executed. They are also sent to our fund
        manager's systems in real time via API through our execution management system. Note that the fund accountant
        scope is not updated in real time. Instead we receive a daily report from our fund accountant which we update
        this scope with each morning before trading begins.
        '''

        # Make a late trade (don't tell them yet)

    def update_fund_accountant_record(self):
        '''
        Early in the morning before trading begins our fund accountant sends us a report with details on yesterday's
        activity and our current position according to their records.

        We will update our fund accountant scope with their records.
        '''
        # Use BY instead of Buy
        pass
    def reconcile_records(self):
        '''
        Now that we have the fund accountant scope updated with this morning's report, we need to see how different the
        fund accountant's view of our position is with our own internal records.

        We can do this by reconciling across all the portfolios inside the two scopes.
        '''
        pass
    def identify_discrepencies(self):
        '''
        So we have identified a number of discrepancies between our internal records and the fund accountant's records.

        Let us try and understand the root cause of these discrepancies
        '''
        # Understand that it was a late trade (where on the timeline do things start to diverge)
        pass
    
    def adjust_portfolio_holdings(self):
        pass
    def change_fund_accountants(self):
        pass

    def test_transparency_oversight(self):
        self.import_data()
        self.create_portfolios()
        self.create_entitlements()
        self.create_holdings()
        self.add_daily_transactions()
        self.update_fund_accountant_record()
        self.reconcile_records()
        self.identify_discrepencies()
        self.adjust_portfolio_holdings()
        self.change_fund_accountants()

if __name__ == '__main__':
    unittest.main()