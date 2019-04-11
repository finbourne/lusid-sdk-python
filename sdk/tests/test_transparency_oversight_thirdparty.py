import unittest
import uuid
import lusid.models as models
import pytz
from datetime import datetime, timedelta, time
from finbournetest import TestFinbourneApi, timeit

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TransparencyOversightThirdParty(TestFinbourneApi):
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

    @timeit
    def import_data(self):
        """
        In LUSID we can create separate environments for our records and those of the fund accountant using Scopes. 
        A Scope is a container which acts as a separate namespace. This allows us to have a portfolio with the same code 
        in different scopes without having to worry about collisions.
        """

        # Create a unique id for our scopes
        internal_scope_id = str(uuid.uuid4())[:8]
        fund_accountant_scope_id = str(uuid.uuid4())[:8]
        # Using the ids create a unique code for each scope, this is what identifies the scope
        self.internal_scope_code = 'internal-{}'.format(internal_scope_id)
        self.fund_accountant_scope_code = 'fund-accountant-{}'.format(fund_accountant_scope_id)
        self.scopes = [self.internal_scope_code, self.fund_accountant_scope_code]

        '''
        We have three clients each with a varying number of portfolios. In LUSID we can use Portfolio Groups to group
        the different portfolios of each of our clients together. Let us create a unique identifier for each client's
        group of portfolios and then we can build our portfolio codes using this id. 
        '''
        # Also create a code for our portfolio, we will re-use the same code in each scope
        self.client_1_portfolio_group_id = str(uuid.uuid4())[:8]
        self.client_2_portfolio_group_id = str(uuid.uuid4())[:8]
        self.client_3_portfolio_group_id = str(uuid.uuid4())[:8]

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
                portfolio_internal = self.transaction_portfolios_api.create_portfolio(scope=self.internal_scope_code,
                                                                                      create_transaction_portfolio_request=portfolio_request)

                # Create our portfolios in the fund accountant scope
                portfolio_fund_accountant = self.transaction_portfolios_api.create_portfolio(
                    scope=self.fund_accountant_scope_code,
                    create_transaction_portfolio_request=portfolio_request)

                # Tests - Ensure that the portfolios were created successfully with the correct details
                self.portfolio_creation_asserts(portfolio_internal, portfolio_request, self.internal_scope_code)
                self.portfolio_creation_asserts(portfolio_fund_accountant, portfolio_request,
                                                self.fund_accountant_scope_code)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object.
            
            This means that unlike when we created the portfolios we need two separate requests to create our groups. 
            One for each scope. 
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
            for scope in self.scopes:
                portfolio_resourceids = [models.ResourceId(scope=scope, code=portfolio_code) for
                                         portfolio_code in portfolio_group]

            # Create our portfolio group requests, note the only difference is in which portfolios we use
            portfolio_group_request = models.CreatePortfolioGroupRequest(id=portfolio_group_code,
                                                                         display_name=portfolio_group_code,
                                                                         values=portfolio_resourceids,
                                                                         description=portfolio_group_code)

            # Create our portfolio groups, note the different scope for each request
            portfolio_group = self.portfolio_groups_api.create_portfolio_group(scope=scope,
                                                                               create_portfolio_group_request=portfolio_group_request)

            # Tests - Ensure that we have successfully created the portfolio groups
            self.portfolio_group_creation_asserts(portfolio_group, portfolio_group_request, scope)

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
        
        Here we can upsert our instruments individually or in a batch. 
        
        You can read more about upserting instruments here: https://docs.lusid.com/#operation/UpsertInstruments
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
            # Create our identifiers
            identifiers = {
                key: models.InstrumentIdValue(
                    value=value) for key, value in instrument['identifiers'].items()
            }

            batch_upsert_request[instrument_name] = models.InstrumentDefinition(
                name=instrument_name,
                identifiers=identifiers)

        # Upsert our batch
        batch_upsert_response = self.instruments_api.upsert_instruments(request_body=batch_upsert_request)

        # Tests - Confirm that the response is as expected
        self.instrument_upsert_asserts(batch_upsert_response, batch_upsert_request)

        '''
        Now that we have our instruments added we can fill our initial holdings to model our live portfolio. 
        
        We will create the holdings data using a nested dictionary. Note that in reality this data would likely come
        from a historical report in a format such as CSV. In this case, a library such as Pandas can be used to 
        handle the data. 
        
        In LUSID the cash is identified by its currency. For example British Pounds is GBP. This is attached to the
        default currency property Instrument/default/Currency
        '''

        self.instrument_universe['GBP_Cash'] = {
            'identifiers': {'ClientInternal': 'GBP'},
            'currency': 'GBP'}

        self.instrument_universe['USD_Cash'] = {
            'identifiers': {'ClientInternal': 'USD'},
            'currency': 'USD'}

        self.client_holdings = {

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
            },

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

        '''
        To set our holdings we use a list of AdjustHoldingRequest objects. We can create these from our holdings data
        above.            
                
        Now that we have our holding adjustments we can set them on our portfolios. Using the set_holdings method
        we can only set holdings on one portfolio at a time. So we will have to iterate over our portfolios and create
        our holdings.
        
        You can read more about creating and setting holding adjustments here: 
        https://docs.lusid.com/#operation/SetHoldings
        
        Note that we have specified an effective at date of today's date minus two days to set the holdings so they
        are up to date as of the day before yesterday.
    
        '''

        holdings_effective_date = (datetime.now(pytz.UTC) - timedelta(days=2)).isoformat()

        # Iterate over our portfolios
        for portfolio_name, portfolio in self.client_holdings.items():

            # Initialise our list to hold the holding adjustments
            holding_adjustments = []

            # Iterate over the holdings in each portfolio
            for instrument_name, holding in portfolio.items():
                # Create our adjust holdings request using our instrument universe to get the LUID identifier for the instrument

                if 'Cash' in instrument_name:
                    identifier_key = 'Instrument/default/Currency'
                else:
                    identifier_key = 'Instrument/default/ClientInternal'

                identifier = self.instrument_universe[instrument_name]['identifiers']['ClientInternal']

                holding_adjustments.append(
                    models.AdjustHoldingRequest(
                        instrument_identifiers={
                            identifier_key: identifier},
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
                        ])
                )

            # Iterate over our two scopes
            for scope in self.scopes:
                set_holdings_response = self.transaction_portfolios_api.set_holdings(scope=scope,
                                                                                     code=portfolio_name,
                                                                                     effective_at=holdings_effective_date,
                                                                                     adjust_holding_request=holding_adjustments)

                # Test to verify that the holdings are correct
                self.verify_holdings_asserts(holding_adjustments=holding_adjustments,
                                             holdings=set_holdings_response,
                                             scope=scope,
                                             code=portfolio_name,
                                             effective_at=holdings_effective_date)

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

        yesterday = datetime.now(pytz.UTC) - timedelta(days=1)
        t = time(hour=8, minute=0)
        self.yesterday_trade_open = pytz.utc.localize(datetime.combine(yesterday, t))
        hours = [1, 5, 3, 8.2, 4, 2, 6, 8.3]

        self.client_transactions = {

            'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['WPP_LondonStockEx_WPP']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[0])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 265600,
                    'transaction_price': 8.9100,
                    'transaction_currency': 'GBP',
                }
            },
            'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Buy',
                    'instrument_uid': self.instrument_universe['MicroFocus_LondonStockEx_MCRO']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[1])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 15074,
                    'transaction_price': 13.2867,
                    'transaction_currency': 'GBP',
                }
            },

            'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['Kingfisher_LondonStockEx_KGF']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[2])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 325000,
                    'transaction_price': 2.3450,
                    'transaction_currency': 'GBP',
                },
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Buy',
                    'instrument_uid': self.instrument_universe['UKGiltTreasury_4.5_2034']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[3])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 10501,
                    'transaction_price': 140.572,
                    'transaction_currency': 'GBP',
                }
            },

            'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Buy',
                    'instrument_uid': self.instrument_universe['UKGiltTreasury_3.75_2021']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[4])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 24000,
                    'transaction_price': 109.126,
                    'transaction_currency': 'GBP',
                },
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['USTreasury_2.00_2021']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[5])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 57000,
                    'transaction_price': 97.80,
                    'transaction_currency': 'USD',
                }
            },

            'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['Whitebread_LondonStockEx_WTB']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[6])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 70000,
                    'transaction_price': 47.03,
                    'transaction_currency': 'GBP',
                },
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['TESCO_LondonStockEx_TSCO']['identifiers'][
                        'ClientInternal'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[7])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 342000,
                    'transaction_price': 1.8865,
                    'transaction_currency': 'GBP',
                }
            }
        }

        '''
        Now that we have defined our trades we can create a batch transaction request for each portfolio. This comes
        in the form of a list of transaction requests.
        
        You can read more about upserting transactions here: https://docs.lusid.com/#operation/UpsertTransactions
        '''

        # Iterate over our portfolios
        for portfolio_name, portfolio in self.client_transactions.items():

            # Initialise a list to hold our transactions for each portfolio
            batch_transaction_requests = []

            # Iterate over the transactions for each portfolio
            for transaction_id, transaction in portfolio.items():
                batch_transaction_requests.append(
                    models.TransactionRequest(transaction_id=transaction_id,
                                              type=transaction['type'],
                                              instrument_identifiers={
                                                  'Instrument/default/ClientInternal': transaction['instrument_uid']},
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

            transaction_response = self.transaction_portfolios_api.upsert_transactions(scope=self.internal_scope_code,
                                                                                       code=portfolio_name,
                                                                                       transaction_request=batch_transaction_requests)

            # Test that the transactions have been added correctly
            self.transactions_added_asserts(portfolio_scope=self.internal_scope_code,
                                            portfolio_code=portfolio_name,
                                            start_date=self.yesterday_trade_open,
                                            end_date=(self.yesterday_trade_open + timedelta(
                                                days=max(hours))).isoformat(),
                                            batch_transactions_request=batch_transaction_requests)

    @timeit
    def update_fund_accountant_record(self):
        """
        It is early in the morning before trading begins and our fund accountant has just sent us the daily report
        with details on yesterday's activity and our current position according to their records.

        We will update our fund accountant scope with their records.
        """

        self.fund_accountant_daily_holdings_report = {

            'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                'WPP_LondonStockEx_WPP': {'quantity': 2690400, 'price': 8.7100},
                'UKGiltTreasury_2.0_2025': {'quantity': 375856, 'price': 8.7100},
                'JustEat_LondonStockEx_JE': {'quantity': 4026354, 'price': 5.4640},
                'UKGiltTreasury_3.75_2021': {'quantity': 486913, 'price': 108.126},
                'GBP_Cash': {'quantity': 5366496, 'price': 1}
            },

            'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                'MicroFocus_LondonStockEx_MCRO': {'quantity': 703068, 'price': 14.5082},
                'Sage_LondonStockEx_SGE': {'quantity': 2599653, 'price': 5.7700},
                'GBP_Cash': {'quantity': 583716.2842, 'price': 1}
            },

            'client-{}-strategy-growth'.format(self.client_1_portfolio_group_id): {
                'BurfordCapital_LondonStockEx_BUR': {'quantity': 853486, 'price': 14.06},
                'EKFDiagnostics_LondonStockEx_EKF': {'quantity': 925925, 'price': 0.2700},
                'GBP_Cash': {'quantity': 150000, 'price': 1}
            },

            'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                'Kingfisher_LondonStockEx_KGF': {'quantity': 1037038, 'price': 2.2760},
                'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                'GBP_Cash': {'quantity': 1714125, 'price': 1}
            },

            'client-{}-strategy-energy'.format(self.client_2_portfolio_group_id): {
                'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                'GBP_Cash': {'quantity': 2200000, 'price': 1}
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
            },

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

        '''
        Now that we have defined our report we can create our holding adjustments. Note that in reality we would
        likely import this report from a csv file or fetch it from an API.
        

        Now that we have our holding adjustments we can set them on our portfolios. Using the set_holdings method
        we can only set holdings on one portfolio at a time. So we will have to iterate over our portfolios and create
        our holdings
        
        This time we use set holdings rather than adjust holdings as we are going to overwrite our existing fund
        accountant scope with the fund accountants report.
        '''

        today = datetime.now(pytz.UTC)
        t = time(hour=6, minute=30)
        self.this_morning = pytz.utc.localize(datetime.combine(today, t)).isoformat()

        for portfolio_name, portfolio in self.fund_accountant_daily_holdings_report.items():

            # Create a key and initialise a list to hold our adjustments for each portfolio
            holding_adjustments = []

            # Iterate over the holdings in each portfolio
            for instrument_name, holding in portfolio.items():
                # Create our adjust holdings request using our instrument universe to get the LUID identifier for the instrument
                if 'Cash' in instrument_name:
                    identifier_key = 'Instrument/default/Currency'
                else:
                    identifier_key = 'Instrument/default/ClientInternal'

                identifier = self.instrument_universe[instrument_name]['identifiers']['ClientInternal']

                holding_adjustments.append(
                    models.AdjustHoldingRequest(
                        instrument_identifiers={
                            identifier_key: identifier},
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
                        ])
                )

            adjust_holdings_response = self.transaction_portfolios_api.adjust_holdings(
                scope=self.fund_accountant_scope_code,
                code=portfolio_name,
                effective_at=self.this_morning,
                adjust_holding_request=holding_adjustments)

            # Tests to verify that the holdings are correct
            self.verify_holdings_asserts(holding_adjustments=holding_adjustments,
                                         holdings=adjust_holdings_response,
                                         scope=self.fund_accountant_scope_code,
                                         code=portfolio_name,
                                         effective_at=self.this_morning)

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

        # Initialise our reconiled portfolios to dictionary to hold any reconciliation breaks
        self.reconciled_portfolios = {}

        # Iterate over our portfolios
        for portfolio_name in self.fund_accountant_daily_holdings_report:

            # Define our internal portfolio
            internal_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                scope=self.internal_scope_code,
                code=portfolio_name),
                effective_at=self.this_morning,
                as_at=datetime.now(pytz.UTC).isoformat())

            # Define our fund accountant portfolio
            fund_accountant_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                scope=self.fund_accountant_scope_code,
                code=portfolio_name),
                effective_at=self.this_morning,
                as_at=datetime.now(pytz.UTC).isoformat())

            # Create our reconciliation request
            reconcile_holdings_request = models.PortfoliosReconciliationRequest(left=internal_portfolio,
                                                                                right=fund_accountant_portfolio,
                                                                                instrument_property_keys=[])

            # Reconcile the two portfolios
            reconciliation = self.reconciliations_api.reconcile_holdings(
                portfolios_reconciliation_request=reconcile_holdings_request)

            # If there are any breaks, add them all to our dictionary
            if reconciliation.count > 0:
                self.reconciled_portfolios[portfolio_name] = reconciliation

                self.reconciliation_asserts(reconciliation,
                                            self.internal_scope_code,
                                            portfolio_name,
                                            self.this_morning,
                                            self.fund_accountant_scope_code,
                                            portfolio_name,
                                            self.this_morning)

        '''
        Okay so looking over our reconciliations we can see that 2 of our portfolios do not reconcile. The rest match
        up which is great. Let's take a look at the difference between these two portfolios in more detail

        We can see that in the first portfolio that the discrepancy is due to our fund accountant portfolio having
        10501 fewer units of an instrument than our own records. We have 87982 units of this
        instrument according to our records, however the fund accountant only has 77481 units. 
        
        We can also see that the fund accountant has more cash than we have on our records. This seems to indicate
        that perhaps a Buy transaction has not gone through.

        We can see that in the second portfolio that the discrepancy is due to our fund accountant portfolio having
        342000 more units of an instrument than our own records. We have 1,864,441 units of this instrument according 
        to our records, and the fund accountant has 2,206,441 units.

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

        self.trade_close_time = (self.yesterday_trade_open + timedelta(hours=8)).isoformat()

        # Initialise our dictionary to hold our reconciliation breaks
        reconciled_portfolios_trade_close = {}

        # Iterate over our portfolios
        for portfolio_name in self.fund_accountant_daily_holdings_report:

            # Internal portfolio
            internal_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                scope=self.internal_scope_code,
                code=portfolio_name),
                effective_at=self.trade_close_time,
                as_at=datetime.now(pytz.UTC).isoformat())
            # Fund accountant portfolio
            fund_accountant_portfolio = models.PortfolioReconciliationRequest(portfolio_id=models.ResourceId(
                scope=self.fund_accountant_scope_code,
                code=portfolio_name),
                effective_at=self.this_morning,
                as_at=datetime.now(pytz.UTC).isoformat())

            # Create our reconciliation request
            reconcile_holdings_request = models.PortfoliosReconciliationRequest(left=internal_portfolio,
                                                                                right=fund_accountant_portfolio,
                                                                                instrument_property_keys=[])

            # Reconcile our two portfolios
            reconciliation = self.reconciliations_api.reconcile_holdings(
                portfolios_reconciliation_request=reconcile_holdings_request)

            # If there are any breaks, add them all to our dictionary
            if reconciliation.count > 0:
                reconciled_portfolios_trade_close[portfolio_name] = reconciliation

                self.reconciliation_asserts(reconciliation,
                                            self.internal_scope_code,
                                            portfolio_name,
                                            self.trade_close_time,
                                            self.fund_accountant_scope_code,
                                            portfolio_name,
                                            self.this_morning)

        '''
        Here we can see that the two portfolios reconcile perfectly. Let's find out what happened after trading. So
        any divergence between our records and those of the fund accountant happened after the close of trading. Let's
        take a look at what transactions happened after this time.
        '''

        late_trades = {}

        for portfolio_name in self.fund_accountant_daily_holdings_report:

            late_trade = self.transaction_portfolios_api.get_transactions(scope=self.internal_scope_code,
                                                                          code=portfolio_name,
                                                                          from_transaction_date=self.trade_close_time,
                                                                          to_transaction_date=self.this_morning)
            if late_trade.count > 0:
                late_trades[portfolio_name] = late_trade

        '''
        Here we can see that there are two trades that happened after this time. We can see one is a buy for 10501
        of one instrument and a sell for 342,000 of another instrument. This corresponds with our reconciliation breaks 
        and thus these must be the missing transactions.
        
        In practice we want to be able to make these checks automatically. This will prevent our investment team
        from having to spend time each morning manually identifying these discrepancies. 
        
        We can do this by comparing our late trades with our reconciliation breaks to identify matched exceptions.
        '''

        # Initialise our dictionary to hold our exceptions
        matched_exceptions = []

        # Iterate over our portfolios and the late trades we have identified
        for portfolio_name, late_trade in late_trades.items():
            # Loop over each late trade
            for trade in late_trade.values:
                # Check if it matches a reconciliation break
                for reconciliation_break in self.reconciled_portfolios[portfolio_name].values:
                    '''
                    Here we use the absolute difference in units to reduce the complexity in identifying if a
                    transaction is a buy or a sell and whether we need to match a positive or negative difference in
                    units. In practice we can add in the ability to check the direction as well
                    '''
                    units = abs(reconciliation_break.difference_units)
                    instrument_uid = reconciliation_break.instrument_uid

                    # If the instrument id and units match, we have identified the cause of the reconciliation break
                    if (trade.instrument_uid == instrument_uid) and (trade.units == units):
                        matched_exceptions.append((trade, reconciliation_break, portfolio_name))

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
        
        You can read more about creating properties here: https://docs.lusid.com/#operation/CreatePropertyDefinition
        '''

        property = models.CreatePropertyDefinitionRequest(domain='Trade',
                                                          scope=self.internal_scope_code,
                                                          code='late_trade',
                                                          value_required=True,
                                                          display_name='late_trade',
                                                          data_type_id=models.ResourceId(scope='default',
                                                                                         code='boolean'))

        self.property_definition_api.create_property_definition(create_property_definition_request=property)

        for exception in matched_exceptions:
            transaction_id = exception[0].transaction_id
            portfolio_name = exception[2]

            r = self.transaction_portfolios_api.add_transaction_property(scope=self.internal_scope_code,
                                                                         code=portfolio_name,
                                                                         transaction_id=transaction_id,
                                                                         request_body={
                                                                             'Trade/{}/late_trade'.format(
                                                                                 self.internal_scope_code):
                                                                                 models.PropertyValue(
                                                                                     label_value='True')})

            self.add_transaction_property_asserts(self.internal_scope_code,
                                                  portfolio_name,
                                                  transaction_id,
                                                  'Trade/{}/late_trade'.format(self.internal_scope_code),
                                                  'True')

    @timeit
    def test_transparency_oversight(self):
        self.import_data()
        self.create_portfolios()
        self.create_holdings()
        self.add_daily_transactions()
        self.update_fund_accountant_record()
        self.reconcile_records()
        self.identify_discrepancies()


if __name__ == '__main__':
    unittest.main()
