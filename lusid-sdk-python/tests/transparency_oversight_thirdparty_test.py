import unittest
import uuid
import lusid.models as models
import pytz
from datetime import datetime, timedelta
from finbournetest import TestFinbourneApi, timeit

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class transparencyOversightThirdParty(TestFinbourneApi):
    @timeit
    def import_data(self):
        """
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
        """

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

    @timeit
    def create_portfolios(self):
        """
        Let us create our portfolios and portfolio groups in both our internal and fund accountant scopes.

        Note that we can only create one portfolio at a time. We will create our portfolios for each client and then
        we will create the portfolio group that holds them.

        These portfolios have been live for 2 years, we just haven't added them to the system yet, so when we
        create them we will specify the date they went live using the 'created' parameter
        """
        portfolio_creation_date = (datetime.now(pytz.UTC) - timedelta(days=895)).isoformat()
        # Iterate over our portfolio groups selecting the name of the group and the list of portfolios
        for portfolio_group_code, portfolio_group in self.client_portfolios.items():
            # Loop over our list of portfolios selecting the portfolio code
            for portfolio_code in portfolio_group:
                # Create the request to add our portfolio
                portfolio_request = models.CreateTransactionPortfolioRequest(display_name=portfolio_code,
                                                                             code=portfolio_code,
                                                                             base_currency='GBP',
                                                                             description=portfolio_code,
                                                                             created=portfolio_creation_date)
                # Create our portfolios in the internal scope
                portfolio_internal = self.client.create_portfolio(scope=self.internal_scope_code,
                                                                  create_request=portfolio_request)

                # Create our portfolios in the fund accountant scope
                portfolio_fund_accountant = self.client.create_portfolio(scope=self.fund_accountant_scope_code,
                                                                         create_request=portfolio_request)

                # Tests - Ensure that the portfolios were created successfully with the correct details
                self.portfolio_creation_tests(portfolio_internal, portfolio_request, self.internal_scope_code)
                self.portfolio_creation_tests(portfolio_fund_accountant, portfolio_request, self.fund_accountant_scope_code)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object.
            
            This means that unlike when we created the portfolios we need two separate requests to create our groups. 
            One for each scope. 
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
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

    @timeit
    def create_entitlements(self):
        pass

    @timeit
    def create_holdings(self):
        """
        Now that we have our portfolios and groups set up for our clients we can add in their current holdings. We will
        start with having the internal scope and the fund account scope completely in sync with exactly the same
        holdings. This will be our initial state.
        """

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
            batch_upsert_request[instrument_name] = models.InstrumentDefinition(name=instrument_name,
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

        We therefore want to add our newly created LUIDs to our initial holdings for future use
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
        
        In LUSID the LUID for cash is the prefix CCY_ followed by the currency. For example British Pounds have a LUID
        of CCY_GBP. We will add these to our instrument universe. 
        '''

        self.instrument_universe['GBP_Cash'] = {
                'identifiers': {'LUID': 'CCY_GBP'},
                'currency': 'GBP'}

        self.instrument_universe['USD_Cash'] = {
                'identifiers': {'LUID': 'CCY_USD'},
                'currency': 'USD'}

        self.client_holdings = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id) : {
                    'WPP_LondonStockEx_WPP': {'quantity': 2956000, 'price': 8.7100},
                    'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                    'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                    'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126},
                    'GBP_Cash': {'quantity': 3000000, 'price': 1}
                },

                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id) : {
                    'MicroFocus_LondonStockEx_MCRO': {'quantity': 687994, 'price': 14.5350},
                    'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700},
                    'GBP_Cash': {'quantity': 784000, 'price': 1}
                },

                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id) : {
                    'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                    'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700},
                    'GBP_Cash': {'quantity': 150000, 'price': 1}
                },

            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id) : {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                    'GBP_Cash': {'quantity': 952000, 'price': 1}
                },

                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id) : {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                    'GBP_Cash': {'quantity': 2200000, 'price': 1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id) : {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'GBP_Cash': {'quantity': 3450000, 'price': 1},
                    'USD_Cash': {'quantity': 1200000, 'price': 1}
                },

                'client-{}-strategy-international'.format(self.client_2_portfolio_group_id) : {
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'Apple_Nasdaq_AAPL': {'quantity': 504481, 'price': 168.49},
                    'Amazon_Nasdaq_AMZN': {'quantity': 38671, 'price': 1629.13},
                    'USD_Cash': {'quantity': 1400000, 'price': 1}
                },

                'client-{}-strategy-usgovt'.format(self.client_2_portfolio_group_id) : {
                    'USTreasury_2.00_2021': {'quantity': 286006, 'price': 97.90},
                    'USTreasury_6.875_2025': {'quantity': 256986, 'price': 124.52},
                    'USD_Cash': {'quantity': 23000000, 'price': 1}
                }

            },

            'client-{}-portfolios'.format(self.client_3_portfolio_group_id) : {

                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id) : {
                    'Whitebread_LondonStockEx_WTB': {'quantity': 355318, 'price': 45.03},
                    'TESCO_LondonStockEx_TSCO': {'quantity': 2206441, 'price': 1.9715},
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 3312829, 'price': 2.276},
                    'UKGiltTreasury_3.75_2021': {'quantity': 128969, 'price': 108.126},
                    'GBP_Cash': {'quantity': 14000000, 'price': 1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_3_portfolio_group_id) : {
                    'UKGiltTreasury_3.5_2045': {'quantity': 286388, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 581411, 'price': 106.637},
                    'USTreasury_2.00_2021': {'quantity': 796731, 'price': 97.9},
                    'USTreasury_6.875_2025': {'quantity': 277063, 'price': 124.52},
                    'GBP_Cash': {'quantity': 1256000, 'price': 1},
                    'USD_Cash': {'quantity': 1570000, 'price': 1}
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
        
        Note that we have specified an effective at date of today's date minus two days to set the holdings so they
        are up to date as of the day before yesterday.
        '''
        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in holding_adjustments.items():
            # Iterate over our portfolios
            for portfolio_name, portfolio_adjustments in portfolio_group.items():

                holdings_internal = self.client.set_holdings(scope=self.internal_scope_code,
                                                             code=portfolio_name,
                                                             effective_at=(datetime.now(pytz.UTC) - timedelta(days=2)).isoformat(),
                                                             holding_adjustments=portfolio_adjustments)

                holdings_fund_accountant = self.client.set_holdings(scope=self.fund_accountant_scope_code,
                                                                    code=portfolio_name,
                                                                    effective_at=(datetime.now(pytz.UTC) - timedelta(days=2)).isoformat(),
                                                                    holding_adjustments=portfolio_adjustments)

                # Tests to verify that the holdings are correct
                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings_internal,
                                           scope=self.internal_scope_code,
                                           code=portfolio_name,
                                           effective_at=(datetime.now(pytz.UTC) - timedelta(days=2)).isoformat())

                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings_fund_accountant,
                                           scope=self.fund_accountant_scope_code,
                                           code=portfolio_name,
                                           effective_at=(datetime.now(pytz.UTC) - timedelta(days=2)).isoformat())

    @timeit
    def add_daily_transactions(self):
        """
        Now that we have our portfolios populated with their holdings we are going to simulate a day of trading. We
        are going to add all of yesterdays transactions to our internal portfolio.

        We had some exciting new strategies to implement across our portfolios that involved

        1) Selling stock in WPP
        2) Buying more stock in MicroFocus
        3) Selling stock in Kingfisher
        4) Buying more of the UK Treasury Gilt maturing in 2034 with coupon rate of 4.5%
        5) Buying some more UK Treasury Gilts and selling US Treasury Bonds
        6) Selling stock in Whitebread
        7) Selling some stock in TESCO

        In reality these trades would be added to our internal scope as soon as they are executed. They are also sent to
        our fund manager's systems in real time via API through our execution management system. Note that the fund
        accountant scope is not updated in real time. Instead we receive a daily report from our fund accountant.
        We then update the fund accountant scope using this report.

        Let us define the trades below. Keeping in mind that these would be generated from our order management or
        execution management system in reality. Each trade has a unique identifier prefixed with tid_. It also has a
        transaction date and settlement date. We can consider datetime.now(pytz.UTC)-timedelta(days=1) to be the start of the
        trading day and the number of hours/days after this to indicate when the trade was executed/settled.
        """

        self.client_transactions = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()) : {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['WPP_LondonStockEx_WPP']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 265600,
                        'transaction_price': 8.9100,
                        'transaction_currency': 'GBP',
                    }
                },
                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['MicroFocus_LondonStockEx_MCRO']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=5)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 15074,
                        'transaction_price': 13.2867,
                        'transaction_currency': 'GBP',
                    }
                }
            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['Kingfisher_LondonStockEx_KGF']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=6)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 325000,
                        'transaction_price': 2.3450,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['UKGiltTreasury_4.5_2034']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 10501,
                        'transaction_price': 140.572,
                        'transaction_currency': 'GBP',
                    }
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['UKGiltTreasury_3.75_2021']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=3)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 24000,
                        'transaction_price': 109.126,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['USTreasury_2.00_2021']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 57000,
                        'transaction_price': 97.80,
                        'transaction_currency': 'USD',
                    }
                },
            },

            'client-{}-portfolios'.format(self.client_3_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['Whitebread_LondonStockEx_WTB']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=5)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 70000,
                        'transaction_price': 47.03,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['TESCO_LondonStockEx_TSCO']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 342000,
                        'transaction_price': 1.8865,
                        'transaction_currency': 'GBP',
                    }
                },
            }
        }

        '''
        Now that we have defined our trades we can create a batch transaction request for each portfolio. This comes
        in the form of a list of transaction requests
        
        Each TransactionRequest object has the following properties:
    
            - transaction_id: A unique transaction identifier tk - unique to what?
            - type: The transaction type, by default the following are already available 
                - 'Buy'
                - 'Sell'
                - 'StockIn'
                - 'StockOut'
                - 'CoverShort'
                - 'SellShort'
                - 'FxBuy'
                - 'FxSell'
                - 'FwdFxBuy'
                - 'FwdFxSell'
                - 'FundsIn'
                - 'FundsOut'
                - 'OLFC' (Open Long Futures Contract)
                - 'CLFC' (Close Long Futures Contract)
                - 'OSFC' (Open Short Futures contract)
                - 'CSFC' (Close Short Futures Contract)
            - instrument_uid: The Lusid Instrument Id also known as LUID
            - transaction_date: The date of the transaction as an ISO8601 datetime, that is "YYYY-MM-DDTHH:MM:SSZ"
            - settlement_date: The date of the settlement as an ISO8601 datetime, that is "YYYY-MM-DDTHH:MM:SSZ"
            - units: The quantity of units of the instrument involved in the transaction
            - transactionPrice: A TransactionPrice object with a price and type
                - price: The price of the transaction
                - type: The type of the price, available options are 'Price', 'Yield' or 'Spread'
            - totalConsideration: The total value of the transaction in settlement currency as a CurrencyAndAmount object
                - amount: The amount of the currency
                - currency: The currency e.g. 'GBP' tk - how do we validate this?
            - exchangeRate: Rate between transaction and settlement currency
            - transactionCurrency: The currency of the transaction
            - source: Where this transaction came from options are 'System' and 'Client'
        '''

        batch_transaction_requests = {}

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in self.client_transactions.items():
            # Create a key for our group to hold the portfolios
            batch_transaction_requests[portfolio_group_name] = {}
            # Iterate over our portfolios
            for portfolio_name, portfolio in portfolio_group.items():
                # Create a key and initialise a list to hold our adjustments for each portfolio
                batch_transaction_requests[portfolio_group_name][portfolio_name] = []
                # Iterate over the holdings in each portfolio
                for transaction_id, transaction in portfolio.items():
                    batch_transaction_requests[portfolio_group_name][portfolio_name].append(
                        models.TransactionRequest(transaction_id=transaction_id,
                                                  type=transaction['type'],
                                                  instrument_uid=transaction['instrument_uid'],
                                                  transaction_date=transaction['transaction_date'],
                                                  settlement_date=transaction['settlement_date'],
                                                  units=transaction['units'],
                                                  transaction_price=models.TransactionPrice(
                                                      price=transaction['transaction_price'],
                                                      type='Price'),
                                                  total_consideration=models.CurrencyAndAmount(
                                                      amount=transaction['units'] * transaction['transaction_price'],
                                                      currency=transaction['transaction_currency']),
                                                  source='Client',
                                                  transaction_currency=transaction['transaction_currency'])
                    )

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in batch_transaction_requests.items():
            # Iterate over our portfolios
            for portfolio_name, portfolio_transactions in portfolio_group.items():
                # If a portfolio has no transactions, skip it
                if len(portfolio_transactions) == 0:
                    continue
                # Upsert our transactions
                internally_recorded_transactions = self.client.upsert_transactions(scope=self.internal_scope_code,
                                                                                   code=portfolio_name,
                                                                                   transactions=portfolio_transactions)

                # Test that the transactions have been added correctly
                self.transactions_added_tests(portfolio_scope=self.internal_scope_code,
                                              portfolio_code=portfolio_name,
                                              start_date=(datetime.now(pytz.UTC) - timedelta(days=1)).isoformat(),
                                              end_date=(datetime.now(pytz.UTC)).isoformat(),
                                              as_at_date=datetime.now(pytz.UTC).isoformat(),
                                              batch_transactions_request=portfolio_transactions)

    @timeit
    def update_fund_accountant_record(self):
        """
        It is early in the morning before trading begins and our fund accountant has just sent us the daily report
        with details on yesterday's activity and our current position according to their records.

        We will update our fund accountant scope with their records.
        """

        self.fund_accountant_daily_holdings_report = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'WPP_LondonStockEx_WPP': {'quantity': 2690400, 'price': 8.7100},
                    'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                    'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                    'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126},
                    'GBP_Cash': {'quantity': 5366496, 'price':1}
                },

                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'MicroFocus_LondonStockEx_MCRO': {'quantity': 703068, 'price': 14.5082},
                    'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700},
                    'GBP_Cash': {'quantity': 583716.2842, 'price':1}
                },

                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id): {
                    'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                    'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700},
                    'GBP_Cash': {'quantity': 150000, 'price':1}
                },

            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1037038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                    'GBP_Cash': {'quantity': 1714125, 'price':1}
                },

                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id): {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                    'GBP_Cash': {'quantity': 2200000, 'price':1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 198800, 'price': 108.247},
                    'USTreasury_2.00_2021': {'quantity': 300507, 'price': 97.90},
                    'USD_Cash': {'quantity': 6774600, 'price': 1},
                    'GBP_Cash': {'quantity': 830976, 'price': 1}
                },

                'client-{}-strategy-international'.format(self.client_2_portfolio_group_id): {
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'Apple_Nasdaq_AAPL': {'quantity': 504481, 'price': 168.49},
                    'Amazon_Nasdaq_AMZN': {'quantity': 38671, 'price': 1629.13},
                    'USD_Cash': {'quantity': 1400000, 'price': 1}
                },

                'client-{}-strategy-usgovt'.format(self.client_2_portfolio_group_id): {
                    'USTreasury_2.00_2021': {'quantity': 286006, 'price': 97.90},
                    'USTreasury_6.875_2025': {'quantity': 256986, 'price': 124.52},
                    'USD_Cash': {'quantity': 23000000, 'price': 1}
                }

            },

            'client-{}-portfolios'.format(self.client_3_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id): {
                    'Whitebread_LondonStockEx_WTB': {'quantity': 285318, 'price': 45.03},
                    'TESCO_LondonStockEx_TSCO': {'quantity': 2206441, 'price': 1.9715},
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 3312829, 'price': 2.276},
                    'UKGiltTreasury_3.75_2021': {'quantity': 128969, 'price': 108.126},
                    'GBP_Cash': {'quantity': 17292100, 'price': 1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_3_portfolio_group_id): {
                    'UKGiltTreasury_3.5_2045': {'quantity': 286388, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 581411, 'price': 106.637},
                    'USTreasury_2.00_2021': {'quantity': 796731, 'price': 97.9},
                    'USTreasury_6.875_2025': {'quantity': 277063, 'price': 124.52},
                    'GBP_Cash': {'quantity': 1256000, 'price': 1},
                    'USD_Cash': {'quantity': 1570000, 'price': 1}
                }
            }
        }

        '''
        Now that we have defined our report we can create our holding adjustments. Note that in reality we would
        likely import this report from a csv file or fetch it from an API.
        '''

        # Initialise our holding adjustments dictionary which will contain a list of adjustments for each portfolio in each portfolio group
        holding_adjustments = {}

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in self.fund_accountant_daily_holdings_report.items():
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
                        models.AdjustHoldingRequest(
                            instrument_uid=self.instrument_universe[instrument_name]['identifiers']['LUID'],
                            tax_lots=[
                                models.TargetTaxLotRequest(units=holding['quantity'],
                                                           cost=models.CurrencyAndAmount(
                                                               amount=holding['quantity'] *
                                                                      holding['price'],
                                                               currency=self.instrument_universe[instrument_name][
                                                                   'currency']),
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
        
        This time we use set holdings rather than adjust holdings tk - why?
        '''

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in holding_adjustments.items():
            # Iterate over our portfolios
            for portfolio_name, portfolio_adjustments in portfolio_group.items():
                holdings = self.client.set_holdings(scope=self.fund_accountant_scope_code,
                                                       code=portfolio_name,
                                                       effective_at=datetime.now(pytz.UTC).isoformat(),
                                                       holding_adjustments=portfolio_adjustments)

                # Tests to verify that the holdings are correct
                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings,
                                           scope=self.fund_accountant_scope_code,
                                           code=portfolio_name,
                                           effective_at=(datetime.now(pytz.UTC)).isoformat())

    @timeit
    def reconcile_records(self):
        """
        Now that we have the fund accountant scope updated with this morning's report, we need to see how different the
        fund accountant's view of our position is with our own internal records.

        We can do this by reconciling across all the portfolios inside the two scopes. We can only reconcile one
        portfolio at a time.

        We can complete a reconciliation by defining the two portfolios to compare as well as the effective date and
        the as at date to use to view the holdings of each portfolio.

        LUSID uses a bi-temporal data store. This means that not only can you reconcile two portfolios as they
        look today, you can also compare how one looks today, compared with how the other looked last week.

        This makes reconciliation much easier and we will take advantage of this if we come across any discrepancies
        between our internal accounts and fund accountant's records.
        """

        self.reconciled_portfolios = {}
        for portfolio_group_name, portfolio_group in self.client_portfolios.items():
            self.reconciled_portfolios[portfolio_group_name] = {}
            for portfolio_name in portfolio_group:

                internal_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                                                                                    scope=self.internal_scope_code,
                                                                                    code=portfolio_name),
                                                                                effective_at=datetime.now(pytz.UTC).isoformat(),
                                                                                as_at=datetime.now(pytz.UTC).isoformat())

                fund_accountant_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                                                                                    scope=self.fund_accountant_scope_code,
                                                                                    code=portfolio_name),
                                                                                 effective_at=datetime.now(pytz.UTC).isoformat(),
                                                                                 as_at=datetime.now(pytz.UTC).isoformat())

                reconcile_holdings_request = models.PortfoliosReconciliationRequest(left=internal_portfolio,
                                                                                    right=fund_accountant_portfolio,
                                                                                    instrument_property_keys=[])

                reconciliation = self.client.reconcile_holdings(request=reconcile_holdings_request)

                if reconciliation.count > 0:
                    self.reconciled_portfolios[portfolio_group_name][portfolio_name] = reconciliation

        '''
        Okay so looking over our reconciliations we can see that 2 of our portfolios do not reconcile. The rest match
        up which is great. Let's take a look at the difference between these two portfolios in more detail
        '''

        # tk - Print detail here for portfolio 1

        '''
        We can see that in the first portfolio that the discrepancy is due to our fund accountant portfolio having
        10501 fewer units of the instrument with LUID_4TMKXHQ7 than our own records. We have 87982 units of this
        instrument according to our records, however the fund accountant only has 77481 units. 
        
        We can also see that the fund accountant has more cash than we have on our records. This seems to indicate
        that perhaps a Buy transaction has not gone through.
        '''

        # tk - Print detail here for portfolio 2

        '''
        We can see that in the second portfolio that the discrepancy is due to our fund accountant portfolio having
        342000 more units of the instrument with LUID_6NGAW9RS than our own records. We have 1,864,441 units of this
        instrument according to our records, and the fund accountant has 2,206,441 units.

        We can also see that the fund accountant has less cash than we have on our records.  This seems to indicate
        that perhaps a Sell transaction has not gone through.
        '''

    @timeit
    def identify_discrepancies(self):
        """
        So we have identified a number of discrepancies between our internal records and the fund accountant's records.
        It seems as though perhaps a buy and a sell transaction have not gone through.

        We do know that the fund accountant finalise their accounts at the close of trade which is 8 hours after trading
        opens each day. Any transactions posted after that won't appear in the next morning's report. Perhaps we had
        some late trades yesterday which caused the issue.

        We can wind back the clock to the close of trade yesterday and see how our two records compare.
        """
        reconciled_portfolios_trade_close = {}
        trade_close_time = (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=8)).isoformat()
        for portfolio_group_name, portfolio_group in self.client_portfolios.items():
            reconciled_portfolios_trade_close[portfolio_group_name] = {}
            for portfolio_name in portfolio_group:

                internal_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                                                                           scope=self.internal_scope_code,
                                                                           code=portfolio_name),
                                                                           effective_at=trade_close_time,
                                                                           as_at=datetime.now(pytz.UTC).isoformat())

                fund_accountant_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                                                                                  scope=self.fund_accountant_scope_code,
                                                                                  code=portfolio_name),
                                                                                  effective_at=datetime.now(pytz.UTC).isoformat(),
                                                                                  as_at=datetime.now(pytz.UTC).isoformat())

                reconcile_holdings_request = models.PortfoliosReconciliationRequest(left=internal_portfolio,
                                                                                    right=fund_accountant_portfolio,
                                                                                    instrument_property_keys=[])

                reconciliation = self.client.reconcile_holdings(request=reconcile_holdings_request)

                if reconciliation.count > 0:
                    reconciled_portfolios_trade_close[portfolio_group_name][portfolio_name] = reconciliation

        '''
        Here we can see that the two portfolios reconcile perfectly. Let's find out what happened after trading. So
        any divergence between our records and those of the fund accountant happened after the close of trading. Let's
        take a look at what transactions happened after this time.
        '''

        late_trades = {}
        for portfolio_group_name, portfolio_group in self.client_portfolios.items():
            late_trades[portfolio_group_name] = {}
            for portfolio_name in portfolio_group:

                late_trade = self.client.get_transactions(scope=self.internal_scope_code,
                                                          code=portfolio_name,
                                                          from_transaction_date=trade_close_time,
                                                          to_transaction_date=datetime.now(pytz.UTC).isoformat())
                if late_trade.count > 0:
                    late_trades[portfolio_group_name][portfolio_name] = late_trade

        #tk - print late trades here

        '''
        Here we can see that there are two trades that happened after this time. We can see one is a buy for 10501
        instruments of LUID_4TMKXHQ7 and one is a sell of 342,000 instruments of LUID_6NGAW9RS. This corresponds
        with our reconciliation breaks and thus these must be the missing transactions.
        
        In practice we want to be able to make these checks automatically. This will prevent our investment team
        from having to spend time each morning manually identifying these discrepancies. 
        
        We can do this by comparing our late trades with our reconciliation breaks to identify matched exceptions.
        '''
        # Initialise our dictionary to hold our exceptions
        matched_exceptions = {}
        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in self.reconciled_portfolios.items():
            # Create a dictionary to hold our portfolios
            matched_exceptions[portfolio_group_name] = {}
            # Iterate over our portfolios and the reconciliation breaks we have identified for them
            for portfolio_name, reconciliation_breaks in portfolio_group.items():
                # Initialise our list to capture exceptions
                matched_exceptions[portfolio_group_name][portfolio_name] = []
                # Iterate over each reconciliation break
                for reconciliation_break in reconciliation_breaks.values:
                    '''
                    Here we use the absolute difference in units to reduce the complexity in identifying if a
                    transaction is a buy or a sell and whether we need to match a positive or negative difference in
                    units. In practice we can add in the ability to check the direction as well
                    '''
                    units = abs(reconciliation_break.difference_units)
                    instrument_uid = reconciliation_break.instrument_uid
                    # Check if there are any late trades for our current portfolio group
                    if len(late_trades[portfolio_group_name]) > 0:
                        # Check if there are any late trades for our current portfolio
                        if portfolio_name in late_trades[portfolio_group_name].keys():
                            # Retrieve our late trade transactions
                            transactions = late_trades[portfolio_group_name][portfolio_name]
                            # Iterate over the transactions
                            for transaction in transactions.values:
                                # If the instrument id and units match, we have identified the cause of the reconciliation break
                                if (transaction.instrument_uid == instrument_uid) and (transaction.units == transaction.units):
                                    matched_exceptions[portfolio_group_name][portfolio_name].append(transaction.transaction_id)

        '''
        Now that we have identified the reason for the reconciliation breaks, we want to flag the transactions in
        question so that we can confirm using tomorrow's report whether or not they have finally been included in the 
        fund accountant's reporting. 
        
        To do this we can use LUSID properties. We can create properties for any object inside LUSID. 
        These properties are defined by us in advance.
        
        In this case we will create a property called 'late_trade' which will be a boolean property that is True if the
        trade has been flagged as a late trade. We will make it so that if we add this property to a trade it is
        required to have the value.
        
        When we set up a property we are required to give it a data type. We do this by specifying a pre-configured
        data type using its ResourceId. Once again this is the scope and code of the object. There are a number of 
        pre-configured types in the default scope which we can draw from. In this case we will use the boolean type.
        This means that when we set the 'late_trade' property we have to specify a value of 'True' or 'False'. 
        '''

        property = models.CreatePropertyDefinitionRequest(domain='Trade',
                                                          scope=self.internal_scope_code,
                                                          code='late_trade',
                                                          value_required=True,
                                                          display_name='late_trade',
                                                          data_type_id=models.ResourceId(scope='default',
                                                                                         code='boolean'))

        self.client.create_property_definition(definition=property)

        for portfolio_group_name, portfolio_group in matched_exceptions.items():
            for portfolio_name, exceptions in portfolio_group.items():
                for transaction_id in exceptions:
                    self.client.add_transaction_property(scope=self.internal_scope_code,
                                                         code=portfolio_name,
                                                         transaction_id=transaction_id,
                                                         transaction_properties={'Trade/{}/late_trade'.format(
                                                             self.internal_scope_code): models.PropertyValue(
                                                             label_value='True')})

                    # tk - test to check that this property has been added successfully

    @timeit
    def change_fund_accountants(self):
        """
        After a few months of reconciling our records with the fund accountant and building algorithms to automatically
        identify exceptions, we have a pretty good idea of the main causes of the discrepancies between our records
        and those of the fund accountant. We have prepared a report with some recommendations for them in order to
        address these causes.

        Unfortunately they don't have much interest in working with us. We have been in talks with another provider
        who can address most of our concerns and have decied to switch fund accountants.

        Fortunately, we have a built up a good cache of historical data inside LUSID and so can easily change providers
        without relying on our incumbent fund accountant to work with the new one.

        To change providers, we can switch our entitlements to give the new accountant access to our records and
        ensure that our old provider no longer has access.
        """

    @timeit
    def test_transparency_oversight(self):
        self.import_data()
        self.create_portfolios()
        self.create_entitlements()
        self.create_holdings()
        self.add_daily_transactions()
        self.update_fund_accountant_record()
        self.reconcile_records()
        self.identify_discrepancies()
        self.change_fund_accountants()

if __name__ == '__main__':
    unittest.main()