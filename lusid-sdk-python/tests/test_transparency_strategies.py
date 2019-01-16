import uuid
import pytz
import unittest
import lusid.models as models
from datetime import datetime, timedelta, time
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
        We are an asset manager who has just taken on a new client. The client has given us a number of mandates on
        how to manage their assets and we have assigned each of these to a different portfolio manager.

        Even though there are a number of different mandates, some of the strategies that we are using are common
        across mandates. We really need to be able to see how each strategy is performing across all of each client's
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
        self.client_2_portfolio_group_id = uuid.uuid4()
        self.client_2_portfolio_group_code = 'client-{}-portfolios'.format(self.client_2_portfolio_group_id)

        self.client_portfolios = [
                'client-{}-mandate-balanced'.format(self.client_2_portfolio_group_id),
                'client-{}-mandate-energy'.format(self.client_2_portfolio_group_id),
                'client-{}-mandate-fixedincome'.format(self.client_2_portfolio_group_id),
                'client-{}-mandate-international'.format(self.client_2_portfolio_group_id),
                'client-{}-mandate-usgovt'.format(self.client_2_portfolio_group_id)
        ]


    @timeit
    def create_portfolios(self):
        """
        Let us create the portfolios for our new client. We will group the client's portfolio's together using a
        portfolio group. A portfolio group is simply a container that can be used to group multiple portfolios
        """

        '''
        Let us create our portfolios and portfolio groups.

        Note that we can only create one portfolio at a time. We will create our portfolios for each client and then
        we will create the portfolio group that holds them.
        
        We onboarded these clients 5 days ago. When we create the portfolios we can set the creation date using the
        'created' argument. This will allow us to backdate holdings and transactions.
        '''
        self.created_date = (datetime.now(pytz.UTC) - timedelta(days=6)).isoformat()
        portfolio_resourceids = []
        # Loop over our list of portfolios selecting the portfolio code
        for portfolio_code in self.client_portfolios:
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
            self.portfolio_creation_asserts(portfolio, portfolio_request, self.internal_scope_code)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object. You can read more about creating portfolio groups here
            https://docs.lusid.com/#operation/CreatePortfolioGroup
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
            portfolio_resourceids.append(models.ResourceId(scope=self.internal_scope_code, code=portfolio_code))

        # Create our portfolio group request
        portfolio_group_request = models.CreatePortfolioGroupRequest(id=self.client_2_portfolio_group_code,
                                                                     display_name=self.client_2_portfolio_group_code,
                                                                     values=portfolio_resourceids,
                                                                     description=self.client_2_portfolio_group_code)

        # Create our portfolio group
        portfolio_group = self.client.create_portfolio_group(scope=self.internal_scope_code,
                                                             request=portfolio_group_request)

        # Tests - Ensure that we have successfully created the portfolio group
        self.portfolio_group_creation_asserts(portfolio_group,
                                              portfolio_group_request,
                                              self.internal_scope_code)

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

        Here we can upsert our instruments individually or in a batch. You can read more about upserting instruments
        here: https://docs.lusid.com/#operation/UpsertInstruments

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
        self.instrument_upsert_asserts(batch_upsert_response, batch_upsert_request)

        '''
        Every instrument that is created is in LUSID given a unique LUSID Instrument Id or LUID for short. This ID is 
        used for many methods and is how the API identifies an instrument. 

        Note that there is also a match feature that allows you to search for instruments using the identifiers that we 
        defined for each instrument, however it is preferred to use the LUID as this is guaranteed to be unique and 
        there is absolutely no chance of a collision. 

        We there want to add our newly created LUIDs to our initial holdings for future use
        '''

        # Loop over our recently upserted instruments
        for instrument_name, instrument in batch_upsert_response.values.items():
            # Add our LUID as a new identifier so that we can use it in our calls later
            self.instrument_universe[instrument_name]['identifiers']['LUID'] = instrument.lusid_instrument_id

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

                'client-{}-mandate-balanced'.format(self.client_2_portfolio_group_id): {
                    'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                    'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                    'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                    'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                    'GBP_Cash': {'quantity': 952000, 'price': 1}
                },

                'client-{}-mandate-energy'.format(self.client_2_portfolio_group_id): {
                    'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                    'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                    'GBP_Cash': {'quantity': 2200000, 'price': 1}
                },

                'client-{}-mandate-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                    'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                    'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'GBP_Cash': {'quantity': 3450000, 'price': 1},
                    'USD_Cash': {'quantity': 1200000, 'price': 1}
                },

                'client-{}-mandate-international'.format(self.client_2_portfolio_group_id): {
                    'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                    'Apple_Nasdaq_AAPL': {'quantity': 504481, 'price': 168.49},
                    'Amazon_Nasdaq_AMZN': {'quantity': 38671, 'price': 1629.13},
                    'USD_Cash': {'quantity': 1400000, 'price': 1}
                },

                'client-{}-mandate-usgovt'.format(self.client_2_portfolio_group_id): {
                    'USTreasury_2.00_2021': {'quantity': 286006, 'price': 97.90},
                    'USTreasury_6.875_2025': {'quantity': 256986, 'price': 124.52},
                    'USD_Cash': {'quantity': 23000000, 'price': 1}
                }

            }


        '''
        To set our holdings we use a list of AdjustHoldingRequest objects. We can create these from our holdings data
        above.

        You can read more about setting holdings here: https://docs.lusid.com/#operation/SetHoldings
        '''

        # Initialise our list to hold the holding adjustments
        for portfolio_name, transactions in self.client_holdings.items():

            stock_in_transactions = []

            # Iterate over the holdings in each portfolio
            for instrument_name, transaction in transactions.items():
                # Create our adjust holdings request using our instrument universe to get the LUID identifier for the instrument
                stock_in_transactions.append(
                    models.TransactionRequest(transaction_id='tid_{}'.format(uuid.uuid4()),
                                              type='StockIn',
                                              instrument_uid=self.instrument_universe[instrument_name]['identifiers'][
                                                  'LUID'],
                                              transaction_date=self.created_date,
                                              settlement_date=self.created_date,
                                              units=transaction['quantity'],
                                              transaction_price=models.TransactionPrice(
                                                  price=transaction['price'],
                                                  type='Price'),
                                              total_consideration=models.CurrencyAndAmount(
                                                  amount=transaction['quantity'] * transaction['price'],
                                                  currency=self.instrument_universe[instrument_name]['currency']),
                                              source='Client',
                                              transaction_currency=self.instrument_universe[instrument_name][
                                                  'currency'])
                )

            upsert_transactions_response = self.client.upsert_transactions(scope=self.internal_scope_code,
                                                                           code=portfolio_name,
                                                                           transactions=stock_in_transactions)

            # Test to verify that the holdings are correct
            self.transactions_added_asserts(portfolio_scope=self.internal_scope_code,
                                            portfolio_code=portfolio_name,
                                            start_date=self.created_date,
                                            end_date=self.created_date,
                                            as_at_date=datetime.now(pytz.UTC).isoformat(),
                                            batch_transactions_request=stock_in_transactions)

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

        You can read more about defining new properties here: https://docs.lusid.com/#operation/CreatePropertyDefinition
        """

        property_request = models.CreatePropertyDefinitionRequest(domain='Trade',
                                                                  scope=self.internal_scope_code,
                                                                  code='strategy',
                                                                  value_required=False,
                                                                  display_name='strategy',
                                                                  data_type_id=models.ResourceId(scope='default',
                                                                                                 code='string'))

        property_response = self.client.create_property_definition(definition=property_request)

        # Grab the key off the response to use when using this property
        self.strategy_property_key = property_response.key

        # Tests to check that the property has been created successfully
        self.create_property_definition_asserts(property_request, property_response)

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

        yesterday = datetime.now(pytz.UTC) - timedelta(days=1)
        t = time(hour=8, minute=0)
        self.yesterday_trade_open = pytz.utc.localize(datetime.combine(yesterday, t))
        hours = [1, 5, 3, 4]

        self.client_transactions = {

            'client-{}-mandate-balanced'.format(self.client_2_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['Kingfisher_LondonStockEx_KGF']['identifiers'][
                        'LUID'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[0])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 325000,
                    'transaction_price': 2.3450,
                    'transaction_currency': 'GBP',
                    'strategy': 'quantitativeSignal'
                },
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Buy',
                    'instrument_uid': self.instrument_universe['UKGiltTreasury_4.5_2034']['identifiers']['LUID'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[1])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 10501,
                    'transaction_price': 140.572,
                    'transaction_currency': 'GBP',
                    'strategy': 'incomeRequirements'
                }
            },

            'client-{}-mandate-fixedincome'.format(self.client_2_portfolio_group_id): {
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Buy',
                    'instrument_uid': self.instrument_universe['UKGiltTreasury_3.75_2021']['identifiers'][
                        'LUID'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[2])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 24000,
                    'transaction_price': 109.126,
                    'transaction_currency': 'GBP',
                    'strategy': 'incomeRequirements'
                },
                'tid_{}'.format(uuid.uuid4()): {
                    'type': 'Sell',
                    'instrument_uid': self.instrument_universe['USTreasury_2.00_2021']['identifiers']['LUID'],
                    'transaction_date': (self.yesterday_trade_open + timedelta(hours=hours[3])).isoformat(),
                    'settlement_date': (self.yesterday_trade_open + timedelta(days=2)).isoformat(),
                    'units': 57000,
                    'transaction_price': 97.80,
                    'transaction_currency': 'USD',
                    'strategy': 'internationalExposure'
                }
            }
        }


        '''
        Now that we have defined our trades we can create a batch transaction request for each portfolio. This comes
        in the form of a list of transaction requests.

        You can read more about adding transactions here: https://docs.lusid.com/#operation/UpsertTransactions
        '''

        # Iterate over our portfolios
        for portfolio_name, transactions in self.client_transactions.items():

            # Initialise a list to hold our transactions for each portfolio
            batch_transaction_requests = []

            # Iterate over the transactions for each portfolio
            for transaction_id, transaction in transactions.items():
                batch_transaction_requests.append(
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
                                                  label_value=transaction['strategy'])}
                                              )
                )

            transaction_response = self.client.upsert_transactions(scope=self.internal_scope_code,
                                                                   code=portfolio_name,
                                                                   transactions=batch_transaction_requests)

            # Test that the transactions have been added correctly
            self.transactions_added_asserts(portfolio_scope=self.internal_scope_code,
                                            portfolio_code=portfolio_name,
                                            start_date=self.yesterday_trade_open.isoformat(),
                                            end_date=(self.yesterday_trade_open + timedelta(
                                                days=max(hours))).isoformat(),
                                            as_at_date=datetime.now(pytz.UTC).isoformat(),
                                            batch_transactions_request=batch_transaction_requests)

            for transaction in batch_transaction_requests:
                self.add_transaction_property_asserts(self.internal_scope_code,
                                                      portfolio_name,
                                                      transaction.transaction_id,
                                                      self.strategy_property_key,
                                                      transaction.properties[self.strategy_property_key].label_value)

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
        On the back of our trades we can look at the overall holdings for our client using the portfolio group we
        created earlier.
        """

        aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                    code='default'),
                                                        effective_at=datetime.now(pytz.UTC).isoformat(),
                                                        metrics=[models.AggregateSpec(key='Holding/default/Units',
                                                                                      op='sum'),
                                                                 models.AggregateSpec(key='Holding/default/Cost',
                                                                                      op='sum')
                                                                  ])

        aggregated_group = self.client.get_aggregation_by_group(scope=self.internal_scope_code,
                                                                code=self.client_2_portfolio_group_code,
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
        portfolio_resourceids = []

        for portfolio_code in self.client_portfolios:
            # Create the request to add our portfolio
            portfolio_request = models.CreateDerivedTransactionPortfolioRequest(display_name=portfolio_code,
                                                                                code=portfolio_code,
                                                                                parent_portfolio_id=models.ResourceId(
                                                                                    scope=self.internal_scope_code,
                                                                                    code=portfolio_code),
                                                                                description=portfolio_code,
                                                                                created=self.created_date,
                                                                                sub_holding_keys=[
                                                                                    self.strategy_property_key])
            # Create our portfolios in the internal scope
            portfolio = self.client.create_derived_portfolio(scope=self.strategy_scope,
                                                             portfolio=portfolio_request)

            # Tests - Ensure that the portfolios were created successfully with the correct details
            self.derived_portfolio_creation_asserts(portfolio, portfolio_request, self.strategy_scope)

            '''
            To create our groups we need the scope and code of each of our portfolios that we want to include in the 
            group. In LUSID these are contained inside a ResourceId object. We use ResourceId objects anytime we need 
            to specify the scope and code of an object.
            '''

            # Create the lists of ResourceIds for each scope, these are the portfolios to add to the group
            portfolio_resourceids.append(models.ResourceId(scope=self.internal_scope_code, code=portfolio_code))

        # Create our portfolio group request
        portfolio_group_request = models.CreatePortfolioGroupRequest(id=self.client_2_portfolio_group_code,
                                                                     display_name=self.client_2_portfolio_group_code,
                                                                     values=portfolio_resourceids,
                                                                     description=self.client_2_portfolio_group_code)

        # Create our portfolio group
        portfolio_group = self.client.create_portfolio_group(scope=self.strategy_scope,
                                                             request=portfolio_group_request)

        # Tests - Ensure that we have successfully created the portfolio group
        self.portfolio_group_creation_asserts(portfolio_group, portfolio_group_request, self.strategy_scope)

        aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                    code='default'),
                                                        effective_at=datetime.now(pytz.UTC).isoformat(),
                                                        metrics=[models.AggregateSpec(key='Holding/default/Units',
                                                                                      op='sum'),
                                                                 models.AggregateSpec(key='Holding/default/Cost',
                                                                                      op='sum')],
                                                        group_by=[self.strategy_property_key, 'Instrument/default/Name'],
                                                        filters=[
                                                            models.PropertyFilter(
                                                                left=self.strategy_property_key,
                                                                operator='NotEquals',
                                                                right='<Not Classified>',
                                                                right_operand_type='Absolute'),
                                                            models.PropertyFilter(
                                                                left='Instrument/default/Name',
                                                                operator='NotEquals',
                                                                right='<Unknown>',
                                                                right_operand_type='Absolute')
                                                               ]
                                                        )

        aggregated_group = self.client.get_aggregation_by_group(scope=self.strategy_scope,
                                                                code=self.client_2_portfolio_group_code,
                                                                request=aggregation_request)

        print ('wait')
        # tk - add test to ensure correct

    @timeit
    def test_transparency_strategies(self):
        self.import_data()
        self.create_portfolios()
        self.add_holdings()
        self.create_strategy_tags()
        self.add_first_transactions()
        self.create_analytics()
        self.aggregate_portfolio_group()
        self.aggregate_strategy()

if __name__ == '__main__':
    unittest.main()