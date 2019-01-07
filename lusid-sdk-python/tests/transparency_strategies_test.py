import uuid
import pytz
import unittest
import lusid.models as models
from datetime import datetime, timedelta
from finbournetest import TestFinbourneApi, timeit

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class transparencyStrategies(TestFinbourneApi):

    @timeit
    def import_data(self):
        """
        We are an asset manager who has just taken on three new clients. Each client has a number of different objectives
        and we will use a different portfolio to track how we are tracking against each objective.

        Even though there are a number of different objectives, some of the strategies that we are using are common
        across objectives. We really need to be able to see how each strategy is performing across all of each client's
        holdings, rather than just looking at a single portfolio in isolation.

        Using LUSID we have the ability to add a strategy label to each transaction that we make. We can then aggregate
        across these labels to get a holistic view into how a strategy is performing.
        """

        '''
        In LUSID every object is contained inside a Scope. A Scope is a container which acts as a separate namespace. 
        '''
        # Create a unique id for our scope
        internal_scope_id = uuid.uuid4()

        # Using the id create a unique code for our scope, this is what identifies the scope
        self.internal_scope_code = 'internal-{}'.format(internal_scope_id)

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
        Let us create the portfolios for our new clients. We will group each client's portfolio's together using a
        portfolio group. A portfolio group is simply a container that can be used to group multiple portfolios
        """

        '''
        Let us create our portfolios and portfolio groups.

        Note that we can only create one portfolio at a time. We will create our portfolios for each client and then
        we will create the portfolio group that holds them.
        
        We onboarded these clients 5 days ago. When we create the portfolios we can set the creation date using the
        'created' argument. This will allow us to backdate holdings and transactions.
        '''
        self.created_date = (datetime.now(pytz.UTC) - timedelta(days=5)).isoformat()
        # Iterate over our portfolio groups selecting the name of the group and the list of portfolios
        for portfolio_group_code, portfolio_group in self.client_portfolios.items():
            # Loop over our list of portfolios selecting the portfolio code
            for portfolio_code in portfolio_group:
                # Create the request to add our portfolio
                portfolio_request = models.CreateTransactionPortfolioRequest(display_name=portfolio_code,
                                                                             code=portfolio_code,
                                                                             base_currency='GBP',
                                                                             description=portfolio_code,
                                                                             created=self.created_date)
                # Create our portfolios in the internal scope
                portfolio = self.client.create_portfolio(scope=self.internal_scope_code,
                                                                  create_request=portfolio_request)

                # Tests - Ensure that the portfolios were created successfully with the correct details
                self.portfolio_creation_tests(portfolio, portfolio_request, self.internal_scope_code)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object.
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
            portfolio_resourceids = [models.ResourceId(scope=self.internal_scope_code, code=portfolio_code) for
                                        portfolio_code in portfolio_group]

            # Create our portfolio group request
            portfolio_group_request = models.CreatePortfolioGroupRequest(id=portfolio_group_code,
                                                                         display_name=portfolio_group_code,
                                                                         values=portfolio_resourceids,
                                                                         description=portfolio_group_code)

            # Create our portfolio group
            portfolio_group = self.client.create_portfolio_group(scope=self.internal_scope_code,
                                                                 request=portfolio_group_request)

            # Tests - Ensure that we have successfully created the portfolio group
            self.portfolio_group_creation_tests(portfolio_group, portfolio_group_request, self.internal_scope_code)

    @timeit
    def add_holdings(self):
        """
        Let us populate our portfolios with their initial holdings
        """

        '''
        Before we can set our holdings we first need to upsert our instrument into LUSID. We use the upsert method which
        will insert a new record if it does not exist and update the existing record if it does exist. This allows us
        to add instruments more simply than checking if an instrument exists before we insert it. 

        Below we have our universe of instruments which all our holdings are made up of. Using LUSID this universe
        can be pre-populated in advance so that we don't have to keep adding new instruments when we make a trade or
        update a holding. 

        Here we can upsert our instruments individually or in a batch. Either way the request should be in the form of a
        dictionary with an arbitrary reference name for the instrument as the key and an InstrumentDefinition object
        as the value.

        The InstrumentDefinition requires a name for the instrument which is a string. In this case we will use the 
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
                                                                                identifiers=instrument[
                                                                                       'identifiers'])
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

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'WPP_LondonStockEx_WPP': {'quantity': 2956000, 'price': 8.7100},
                    'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                    'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                    'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126},
                    'GBP_Cash': {'quantity': 3000000, 'price': 1}
                },

                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'MicroFocus_LondonStockEx_MCRO': {'quantity': 687994, 'price': 14.5350},
                    'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700},
                    'GBP_Cash': {'quantity': 784000, 'price': 1}
                },

                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id): {
                    'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                    'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700},
                    'GBP_Cash': {'quantity': 150000, 'price': 1}
                },

            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                    'GBP_Cash': {'quantity': 952000, 'price': 1}
                },

                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id): {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                    'GBP_Cash': {'quantity': 2200000, 'price': 1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'GBP_Cash': {'quantity': 3450000, 'price': 1},
                    'USD_Cash': {'quantity': 1200000, 'price': 1}
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
                    'Whitebread_LondonStockEx_WTB': {'quantity': 355318, 'price': 45.03},
                    'TESCO_LondonStockEx_TSCO': {'quantity': 2206441, 'price': 1.9715},
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 3312829, 'price': 2.276},
                    'UKGiltTreasury_3.75_2021': {'quantity': 128969, 'price': 108.126},
                    'GBP_Cash': {'quantity': 14000000, 'price': 1}
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

        Note that we have specified an effective at date of 5 days ago when the portfolio was created.
        '''
        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in holding_adjustments.items():
            # Iterate over our portfolios
            for portfolio_name, portfolio_adjustments in portfolio_group.items():
                holdings = self.client.set_holdings(scope=self.internal_scope_code,
                                                    code=portfolio_name,
                                                    effective_at=self.created_date,
                                                    holding_adjustments=portfolio_adjustments)

                # Tests to verify that the holdings are correct
                self.verify_holdings_tests(holding_adjustments=portfolio_adjustments,
                                           holdings=holdings,
                                           scope=self.internal_scope_code,
                                           code=portfolio_name,
                                           effective_at=self.created_date)

    @timeit
    def add_holdings_via_transactions(self):
        """
        Let us populate our portfolios with their initial holdings
        """

        '''
        Before we can set our holdings we first need to upsert our instrument into LUSID. We use the upsert method which
        will insert a new record if it does not exist and update the existing record if it does exist. This allows us
        to add instruments more simply than checking if an instrument exists before we insert it. 

        Below we have our universe of instruments which all our holdings are made up of. Using LUSID this universe
        can be pre-populated in advance so that we don't have to keep adding new instruments when we make a trade or
        update a holding. 

        Here we can upsert our instruments individually or in a batch. Either way the request should be in the form of a
        dictionary with an arbitrary reference name for the instrument as the key and an InstrumentDefinition object
        as the value.

        The InstrumentDefinition requires a name for the instrument which is a string. In this case we will use the 
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
                                                                                identifiers=instrument[
                                                                                       'identifiers'])
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

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'WPP_LondonStockEx_WPP': {'quantity': 2956000, 'price': 8.7100},
                    'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                    'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                    'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126},
                    'GBP_Cash': {'quantity': 3000000, 'price': 1}
                },

                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'MicroFocus_LondonStockEx_MCRO': {'quantity': 687994, 'price': 14.5350},
                    'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700},
                    'GBP_Cash': {'quantity': 784000, 'price': 1}
                },

                'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id): {
                    'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                    'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700},
                    'GBP_Cash': {'quantity': 150000, 'price': 1}
                },

            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                    'GBP_Cash': {'quantity': 952000, 'price': 1}
                },

                'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id): {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                    'GBP_Cash': {'quantity': 2200000, 'price': 1}
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'GBP_Cash': {'quantity': 3450000, 'price': 1},
                    'USD_Cash': {'quantity': 1200000, 'price': 1}
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
                    'Whitebread_LondonStockEx_WTB': {'quantity': 355318, 'price': 45.03},
                    'TESCO_LondonStockEx_TSCO': {'quantity': 2206441, 'price': 1.9715},
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 3312829, 'price': 2.276},
                    'UKGiltTreasury_3.75_2021': {'quantity': 128969, 'price': 108.126},
                    'GBP_Cash': {'quantity': 14000000, 'price': 1}
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
        To set our holdings we will upsert transactions for each holding using the 'StockIn' transaction type
        '''

        # Initialise our holding adjustments dictionary which will contain a list of adjustments for each portfolio in each portfolio group
        batch_transaction_requests = {}

        # Iterate over our portfolio groups
        for portfolio_group_name, portfolio_group in self.client_holdings.items():
            # Create a key for our group to hold the portfolios
            batch_transaction_requests[portfolio_group_name] = {}
            # Iterate over our portfolios
            for portfolio_name, portfolio in portfolio_group.items():
                # Create a key and initialise a list to hold our adjustments for each portfolio
                batch_transaction_requests[portfolio_group_name][portfolio_name] = []
                # Iterate over the holdings in each portfolio
                for instrument_name, holding in portfolio.items():
                    # Create our adjust holdings request using our instrument universe to get the LUID identifier for the instrument
                    batch_transaction_requests[portfolio_group_name][portfolio_name].append(
                        models.TransactionRequest(transaction_id='tid_{}'.format(uuid.uuid4()),
                                                  type='StockIn',
                                                  instrument_uid=self.instrument_universe[instrument_name]['identifiers']['LUID'],
                                                  transaction_date=self.created_date,
                                                  settlement_date=self.created_date,
                                                  units=holding['quantity'],
                                                  transaction_price=models.TransactionPrice(
                                                      price=holding['price'],
                                                      type='Price'),
                                                  total_consideration=models.CurrencyAndAmount(
                                                      amount=holding['quantity'] * holding['price'],
                                                      currency=self.instrument_universe[instrument_name]['currency']),
                                                  source='Client',
                                                  transaction_currency=self.instrument_universe[instrument_name]['currency'])
                    )


        '''
        Now that we have our holding adjustments we can set them on our portfolios. Using the set_holdings method
        we can only set holdings on one portfolio at a time. So we will have to iterate over our portfolios and create
        our holdings

        Note that we have specified an effective at date of 5 days ago when the portfolio was created.
        '''
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
                                              start_date=self.created_date,
                                              end_date=self.created_date,
                                              as_at_date=self.created_date,
                                              batch_transactions_request=portfolio_transactions)

    @timeit
    def create_strategy_tags(self):
        """
        Now that we have our portfolios we can create our strategy label. In LUSID we do this using what is known as
        a property. A property is user defined in advance and can be set on any LUSID object. We are going to create
        a property called 'strategy' which will take the value of a string. We will attach this property to each
        transaction. The string will be the name of the strategy that we are following when making the transaction.

        Each property sits inside a domain. This domain tells us which LUSID objects we can attach the property
        to. In this case we want to attach our property to transactions so we use the 'Trade' domain. Other options
        are "Portfolio", "Security", "Holding", "ReferenceHolding", "TxnType", "Instrument" and "CutDefinition".

        When we set up a property we are required to give it a data type. We do this by specifying a data type using its
        ResourceId. Once again this is the scope and code of the object. There are a number of pre-configured types in
        the default scope which we can draw from. We can also create our own types. In this case we will use the
        default string type.

        This means that when we set the 'strategy' property we can use any string we like as the label.
        """

        property_request = models.CreatePropertyDefinitionRequest(domain='Trade',
                                                                  scope=self.internal_scope_code,
                                                                  code='strategy',
                                                                  value_required=True,
                                                                  display_name='strategy',
                                                                  data_type_id=models.ResourceId(scope='default',
                                                                                                 code='string'))

        property = self.client.create_property_definition(definition=property_request)

        # Grab the key off the response to use when using this property
        self.strategy_property_key = property.key

        # Tests to check that the property has been created successfully
        self.create_property_definition_test(property_request, property)

    @timeit
    def add_first_transactions(self):
        """
        Now that we have defined our strategy tag property for use on our transactions, we can make some trades
        for our new clients attaching the appropriate tag to each trade.
        """

        '''
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

        In reality these trades would be added to our internal scope as soon as they are executed. 
        
        Let us define the trades below. Keeping in mind that these would be generated from our order management or
        execution management system in reality. Each trade has a unique identifier prefixed with tid_. It also has a
        transaction date and settlement date. We can consider datetime.now(pytz.UTC)-timedelta(days=1) to be the start of the
        trading day and the number of hours/days after this to indicate when the trade was executed/settled.
        '''

        self.client_transactions = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['WPP_LondonStockEx_WPP']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 265600,
                        'transaction_price': 8.9100,
                        'transaction_currency': 'GBP',
                        'strategy': 'quantitativeSignal'
                    }
                },
                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['MicroFocus_LondonStockEx_MCRO']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=5)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 15074,
                        'transaction_price': 13.2867,
                        'transaction_currency': 'GBP',
                        'strategy': 'fundamentalAnalysis'
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
                        'strategy': 'quantitativeSignal'
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['UKGiltTreasury_4.5_2034']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 10501,
                        'transaction_price': 140.572,
                        'transaction_currency': 'GBP',
                        'strategy': 'incomeRequirements'
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
                        'strategy': 'incomeRequirements'
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['USTreasury_2.00_2021']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 57000,
                        'transaction_price': 97.80,
                        'transaction_currency': 'USD',
                        'strategy': 'internationalExposure'
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
                        'strategy': 'fundamentalAnalysis'
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['TESCO_LondonStockEx_TSCO']['identifiers']['LUID'],
                        'transaction_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.now(pytz.UTC) - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 342000,
                        'transaction_price': 1.8865,
                        'transaction_currency': 'GBP',
                        'strategy': 'quantitativeSignal'
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
            - properties: A dictionary of properties with the key as the domain/scope/code of the property we defined
                          earlier and a value of the value for the property
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
                                                  transaction_currency=transaction['transaction_currency'],
                                                  properties={self.strategy_property_key: models.PropertyValue(
                                                      label_value=transaction['strategy'])})
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
                                              end_date=datetime.now(pytz.UTC).isoformat(),
                                              as_at_date=datetime.now(pytz.UTC).isoformat(),
                                              batch_transactions_request=portfolio_transactions)

                # tk - add test for properties

    @timeit
    def create_analytics(self):
        """
        To run aggregation over our portfolio groups we first need to define an analytic store
        """

        analytics_effective_date = datetime.now(pytz.UTC)

        # Create analytics store
        analytics_store_request = models.CreateAnalyticStoreRequest(scope=self.internal_scope_code,
                                                                    date_property=analytics_effective_date.isoformat())

        self.client.create_analytic_store(request=analytics_store_request)

        # Create prices via instrument, analytic
        instrument_analytics = []

        for instrument_name, instrument in self.instrument_universe.items():
            if 'Cash' in instrument_name:
                continue
            instrument_analytics.append(models.InstrumentAnalytic(instrument_uid=instrument['identifiers']['LUID'],
                                                                  value=1))

        # Set my analytics
        self.client.set_analytics(scope=self.internal_scope_code,
                                  year=analytics_effective_date.year,
                                  month=analytics_effective_date.month,
                                  day=analytics_effective_date.day,
                                  data=instrument_analytics)

    @timeit
    def aggregate_portfolio_group(self):
        """
        On the back of our trades we can look at the holdings for each of our clients using the portfolio groups we
        created earlier.
        """

        for portfolio_group_code, portfolio_group in self.client_portfolios.items():
            aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                        code='default'),
                                                            effective_at=datetime.now(pytz.UTC).isoformat(),
                                                            metrics=[models.AggregateSpec(key='Holding/default/Units',
                                                                                          op='sum'),
                                                                     models.AggregateSpec(key='Holding/default/Cost',
                                                                                          op='sum')
                                                                      ])

            aggregated_group = self.client.get_aggregation_by_group(scope=self.internal_scope_code,
                                                                    code=portfolio_group_code,
                                                                    request=aggregation_request)

            # tk - Tests to confirm correct, how?

    @timeit
    def aggregate_strategy(self):
        """
        We can also look at how a given strategy is performing across our client's entire holdings. To do this we can
        apply a filter to our aggregated result.
        """
        strategy = ''
        scope_id = uuid.uuid4()
        self.strategy_scope = 'strategy-scope-{}'.format(scope_id)

        # Create our derived portfolios
        self.created_date = (datetime.now(pytz.UTC) - timedelta(days=5)).isoformat()
        # Iterate over our portfolio groups selecting the name of the group and the list of portfolios
        for portfolio_group_code, portfolio_group in self.client_portfolios.items():
            # Loop over our list of portfolios selecting the portfolio code
            for portfolio_code in portfolio_group:
                # Create the request to add our portfolio
                portfolio_request = models.CreateDerivedTransactionPortfolioRequest(display_name=portfolio_code,
                                                                                    code=portfolio_code,
                                                                                    parent_portfolio_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                                                          code=portfolio_code),
                                                                                    description=portfolio_code,
                                                                                    created=self.created_date,
                                                                                    sub_holding_keys=[self.strategy_property_key])
                # Create our portfolios in the internal scope
                portfolio = self.client.create_derived_portfolio(scope=self.strategy_scope,
                                                                 portfolio=portfolio_request)

                # Tests - Ensure that the portfolios were created successfully with the correct details
                self.derived_portfolio_creation_tests(portfolio, portfolio_request, self.strategy_scope)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object.
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
            portfolio_resourceids = [models.ResourceId(scope=self.strategy_scope, code=portfolio_code) for
                                     portfolio_code in portfolio_group]

            # Create our portfolio group request
            portfolio_group_request = models.CreatePortfolioGroupRequest(id=portfolio_group_code,
                                                                         display_name=portfolio_group_code,
                                                                         values=portfolio_resourceids,
                                                                         description=portfolio_group_code)

            # Create our portfolio group
            portfolio_group = self.client.create_portfolio_group(scope=self.strategy_scope,
                                                                 request=portfolio_group_request)

            # Tests - Ensure that we have successfully created the portfolio group
            self.portfolio_group_creation_tests(portfolio_group, portfolio_group_request, self.strategy_scope)


        for portfolio_group_code, portfolio_group in self.client_portfolios.items():

            aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                        code='default'),
                                                            effective_at=datetime.now(pytz.UTC).isoformat(),
                                                            metrics=[models.AggregateSpec(key='Holding/default/Units',
                                                                                          op='sum'),
                                                                     models.AggregateSpec(key='Holding/default/Cost',
                                                                                          op='sum')],
                                                            group_by=[self.strategy_property_key, 'Instrument/default/Name'],
                                                            filters=[models.PropertyFilter(left=self.strategy_property_key,
                                                                                           operator='NotEquals',
                                                                                           right='<Not Classified>',
                                                                                           right_operand_type='Absolute'
                                                                                           ),
                                                                     models.PropertyFilter(
                                                                         left='Instrument/default/Name',
                                                                         operator='NotEquals',
                                                                         right='<Unknown>',
                                                                         right_operand_type='Absolute'
                                                                         )
                                                                     ])

            aggregated_group = self.client.get_aggregation_by_group(scope=self.strategy_scope,
                                                                    code=portfolio_group_code,
                                                                    request=aggregation_request)

            print ('test')
            # tk - add test to ensure correct

    @timeit
    def test_transparency_strategies(self):
        self.import_data()
        self.create_portfolios()
        self.add_holdings()
        #self.add_holdings_via_transactions()
        self.create_strategy_tags()
        self.add_first_transactions()
        self.create_analytics()
        self.aggregate_portfolio_group()
        self.aggregate_strategy()

if __name__ == '__main__':
    unittest.main()