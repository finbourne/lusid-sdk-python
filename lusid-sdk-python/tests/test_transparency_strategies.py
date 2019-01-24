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


class TransparencyStrategies(TestFinbourneApi):
    """
    We are an asset manager who has just taken on a new client. The client has given us a number of mandates on
    how to manage their assets and we have assigned each of these to a different portfolio manager.

    Even though there are a number of different mandates, some of the strategies that we are using are common
    across mandates. We really need to be able to see how each strategy is performing across all of our client's
    holdings, rather than just looking at a single portfolio in isolation.

    Using LUSID we have the ability to add a strategy label to each transaction that we make. We can then aggregate
    across these labels to get a holistic view into how a strategy is performing.
    """

    @timeit
    def import_data(self):
        """
        This method is used to initialise our environment and define some of the data that we will use.
        """

        '''
        In LUSID almost every object is contained inside a Scope. A Scope is a container which acts as a separate 
        namespace. We will create an internal Scope to hold our client's portfolio. 
        '''
        # Let us create an internal scope with a unique identifier
        self.internal_scope_code = 'internal-{}'.format(uuid.uuid4())

        '''
        Inside each scope an object can be identified via its unique Code. For our client we will create a unique 
        identifier to use in the name of each of their portfolios. We wil also create a code to use when we create a
        portfolio group to group all of our client's portfolios together.
        '''
        # Create a unique identifier for our client
        self.client_id = uuid.uuid4()
        # Create the codes for our portfolios, each of which have a different mandate
        self.client_portfolios = [
            'client-{}-mandate-balanced'.format(self.client_id),
            'client-{}-mandate-energy'.format(self.client_id),
            'client-{}-mandate-fixedincome'.format(self.client_id),
            'client-{}-mandate-international'.format(self.client_id),
            'client-{}-mandate-usgovt'.format(self.client_id)
        ]
        # Create a unique code for our portfolio group.
        self.client_portfolio_group_code = 'client-{}-portfolios'.format(self.client_id)

    @timeit
    def create_portfolios(self):
        """
        This method is used to create the portfolios for our new client. We will group the client's portfolio's
        together using a portfolio group. A portfolio group is simply a container that can be used to group multiple
        portfolios.
        """

        '''
        Note that in LUSID we can only create one portfolio at a time. 
        
        We will thus create each of the portfolios for our client one at a time and then we will create the portfolio 
        group that holds them together.
        
        We on-boarded this clients 5 days ago. When we create the portfolios we can set the creation date using the
        'created' argument. This will allow us to backdate holdings and transactions.
        
        You can read more about portfolio creation here: https://docs.lusid.com/#operation/CreatePortfolio
        You can read more about portfolio group creation here: https://docs.lusid.com/#operation/CreatePortfolioGroup
        '''
        # Set the creation date of our portfolio
        self.created_date = datetime.now(pytz.UTC) - timedelta(days=5)
        # Initialise a list to hold the ids of our portfolios for use in creating our portfolio group
        portfolio_resourceids = []
        # Loop over our portfolios
        for portfolio_code in self.client_portfolios:
            # Create the request to add our portfolio
            portfolio_request = models.CreateTransactionPortfolioRequest(display_name=portfolio_code,
                                                                         code=portfolio_code,
                                                                         base_currency='GBP',
                                                                         description=portfolio_code,
                                                                         created=self.created_date.isoformat())
            # Call LUSID to create our portfolio
            portfolio = self.client.create_portfolio(scope=self.internal_scope_code,
                                                     create_request=portfolio_request)

            # Test - Ensure that the portfolio was created successfully with the correct details
            self.portfolio_creation_asserts(portfolio, portfolio_request, self.internal_scope_code)

            # Add the portfolio to our list of portfolios for the portfolio group
            portfolio_resourceids.append(models.ResourceId(scope=self.internal_scope_code, code=portfolio_code))

        # Create our portfolio group request
        portfolio_group_request = models.CreatePortfolioGroupRequest(id=self.client_portfolio_group_code,
                                                                     display_name=self.client_portfolio_group_code,
                                                                     values=portfolio_resourceids,
                                                                     description='Grouping all of client {} portfolios'
                                                                     .format(self.client_id))

        # Call LUSID to create our portfolio group
        portfolio_group = self.client.create_portfolio_group(scope=self.internal_scope_code,
                                                             request=portfolio_group_request)

        # Test - Ensure that we have successfully created the portfolio group
        self.portfolio_group_creation_asserts(portfolio_group, portfolio_group_request, self.internal_scope_code)

    @timeit
    def add_holdings(self):
        """
        This method loads our take on balances, which may also be referred to as our initial holdings to our client's
        portfolios.
        """

        '''
        Before we can load our take on balances we first need to add securities to our instrument master in LUSID. 
        
        This contains the details of all of the securities that we hold or trade in. Any time that we conduct a trade
        or add a holding of a security we refer to it in the instrument master. 
        
        To add securities to the instrument master we use an upsert method. This method will insert a new record if it 
        does not exist and update the existing record if it does exist. This allows us to add instruments more simply 
        than have to check if an instrument exists before we insert it. 

        Below we have our universe of instruments which all of our holdings are made up of. Using LUSID this universe
        can be pre-populated in advance so that we don't have to keep adding new instruments when we make a trade or
        update a holding. 

        We can upsert our instruments individually or in a batch. You can read more about upserting instruments
        here: https://docs.lusid.com/#operation/UpsertInstruments
        '''

        self.instrument_universe = {
            'WPP_LondonStockEx_WPP': {
                'identifiers': {'ClientInternal': 'JE00B8KF9B49'},
                'currency': 'GBP'},

            'UKGiltTreasury_3.5_2045': {
                'identifiers': {'ClientInternal': 'GB00BN65R313'},
                'currency': 'GBP'},

            'UKGiltTreasury_2.0_2025': {
                'identifiers': {'ClientInternal': 'GB00BTHH2R79'},
                'currency': 'GBP'},

            'UKGiltTreasury_4.5_2034': {
                'identifiers': {'ClientInternal': 'GB00B52WS153'},
                'currency': 'GBP'},

            'UKGiltTreasury_3.75_2021': {
                'identifiers': {'ClientInternal': 'GB00B4RMG977'},
                'currency': 'GBP'},

            'Kingfisher_LondonStockEx_KGF': {
                'identifiers': {'ClientInternal': 'GB0033195214'},
                'currency': 'GBP'},

            'JustEat_LondonStockEx_JE': {
                'identifiers': {'ClientInternal': 'GB00BKX5CN86'},
                'currency': 'GBP'},

            'RELXGroup_LondonStockEx_REL': {
                'identifiers': {'ClientInternal': 'GB00B2B0DG97'},
                'currency': 'GBP'},

            'TESCO_LondonStockEx_TSCO': {
                'identifiers': {'ClientInternal': 'GB0008847096'},
                'currency': 'GBP'},

            'Whitebread_LondonStockEx_WTB': {
                'identifiers': {'ClientInternal': 'GB00B1KJJ408'},
                'currency': 'GBP'},

            'USTreasury_2.00_2021': {
                'identifiers': {'ClientInternal': 'US912828U816'},
                'currency': 'USD'},

            'USTreasury_6.875_2025': {
                'identifiers': {'ClientInternal': 'US912810EV62'},
                'currency': 'USD'},

            'BP_LondonStockEx_BP': {
                'identifiers': {'ClientInternal': 'GB0007980591'},
                'currency': 'GBP'},

            'MicroFocus_LondonStockEx_MCRO': {
                'identifiers': {'ClientInternal': 'GB00BD8YWM01'},
                'currency': 'GBP'},

            'Sage_LondonStockEx_SGE': {
                'identifiers': {'ClientInternal': 'GB00B8C3BL03'},
                'currency': 'GBP'},

            'BurfordCapital_LondonStockEx_BUR': {
                'identifiers': {'ClientInternal': 'GG00B4L84979'},
                'currency': 'GBP'},

            'EKFDiagnostics_LondonStockEx_EKF': {
                'identifiers': {'ClientInternal': 'GB0031509804'},
                'currency': 'GBP'},

            'Apple_Nasdaq_AAPL': {
                'identifiers': {'ClientInternal': 'US0378331005'},
                'currency': 'USD'},

            'Amazon_Nasdaq_AMZN': {
                'identifiers': {'ClientInternal': 'US0231351067'},
                'currency': 'USD'},

            'Glencore_LondonStockEx_GLEN': {
                'identifiers': {'ClientInternal': 'JE00B4T3BW64'},
                'currency': 'GBP'}
        }

        # Initialise our batch upsert request
        batch_upsert_request = {}
        # Using our instrument universe create our batch request
        for instrument_name, instrument in self.instrument_universe.items():
            batch_upsert_request[instrument_name] = models.InstrumentDefinition(name=instrument_name,
                                                                                identifiers=instrument['identifiers'])
        # Call LUSID to upsert our batch
        batch_upsert_response = self.client.upsert_instruments(requests=batch_upsert_request)

        # Tests - Confirm that all instruments have been successfully upserted
        self.instrument_upsert_asserts(batch_upsert_response, batch_upsert_request)

        '''
        Every instrument that is created is in LUSID given a unique LUSID Instrument Id or LUID for short. This ID is 
        used for many methods and is how LUSID uniquely identifies an instrument.

        We therefore want to add our newly created LUIDs to our local instrument universe for later use.
        
        In addition in LUSID there are default cash securities available to us. The LUID for cash is the prefix CCY_ 
        followed by the currency. For example British Pounds have a LUID of CCY_GBP. We will aslo add these to our local
        instrument universe. 
        '''
        # Loop over our recently upserted instruments
        for instrument_name, instrument in batch_upsert_response.values.items():
            # Add our LUID as a new identifier so that we can use it in our calls later
            self.instrument_universe[instrument_name]['identifiers']['LUID'] = instrument.lusid_instrument_id

        self.instrument_universe['GBP_Cash'] = {
            'identifiers': {'LUID': 'CCY_GBP'},
            'currency': 'GBP'}

        self.instrument_universe['USD_Cash'] = {
            'identifiers': {'LUID': 'CCY_USD'},
            'currency': 'USD'}

        '''
        Now that we have our securities added to our instrument master we can load our take on balances.

        We will do this by adding our take on balances as 'StockIn' transactions. 
        
        You can read more about upserting transactions here: https://docs.lusid.com/#operation/UpsertTransactions
        '''

        self.client_holdings = {

            'client-{}-mandate-balanced'.format(self.client_id): {
                'Kingfisher_LondonStockEx_KGF': {'quantity': 1362038, 'price': 2.2760},
                'JustEat_LondonStockEx_JE': {'quantity': 834553, 'price': 5.4640},
                'RELXGroup_LondonStockEx_REL': {'quantity': 494343, 'price': 15.98},
                'UKGiltTreasury_4.5_2034': {'quantity': 77481, 'price': 140.572},
                'GBP_Cash': {'quantity': 952000, 'price': 1}
            },

            'client-{}-mandate-energy'.format(self.client_id): {
                'Glencore_LondonStockEx_GLEN': {'quantity': 905141, 'price': 2.7620},
                'BP_LondonStockEx_BP': {'quantity': 1713922, 'price': 5.1140},
                'GBP_Cash': {'quantity': 2200000, 'price': 1}
            },

            'client-{}-mandate-fixedincome'.format(self.client_id): {
                'UKGiltTreasury_3.5_2045': {'quantity': 266169, 'price': 134.433},
                'UKGiltTreasury_2.0_2025': {'quantity': 405589, 'price': 106.637},
                'UKGiltTreasury_3.75_2021': {'quantity': 174800, 'price': 108.126},
                'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                'GBP_Cash': {'quantity': 3450000, 'price': 1},
                'USD_Cash': {'quantity': 1200000, 'price': 1}
            },

            'client-{}-mandate-international'.format(self.client_id): {
                'USTreasury_2.00_2021': {'quantity': 357507, 'price': 97.90},
                'Apple_Nasdaq_AAPL': {'quantity': 504481, 'price': 168.49},
                'Amazon_Nasdaq_AMZN': {'quantity': 38671, 'price': 1629.13},
                'USD_Cash': {'quantity': 1400000, 'price': 1}
            },

            'client-{}-mandate-usgovt'.format(self.client_id): {
                'USTreasury_2.00_2021': {'quantity': 286006, 'price': 97.90},
                'USTreasury_6.875_2025': {'quantity': 256986, 'price': 124.52},
                'USD_Cash': {'quantity': 23000000, 'price': 1}
            }

        }
        # Set the date from which the take on balances should be effective, in this case one day after on-boarding
        self.effective_date = self.created_date + timedelta(days=1)
        # Iterate over our portfolios
        for portfolio_name, transactions in self.client_holdings.items():
            # Initialise our list to hold the transactions
            stock_in_transactions = []
            # Iterate over the transactions in each portfolio
            for instrument_name, transaction in transactions.items():
                # Create our request using our instrument universe to get the LUID identifier for the instrument
                stock_in_transactions.append(
                    models.TransactionRequest(transaction_id='tid_{}'.format(uuid.uuid4()),
                                              type='StockIn',
                                              instrument_uid=self.instrument_universe[instrument_name]['identifiers'][
                                                  'LUID'],
                                              transaction_date=self.effective_date.isoformat(),
                                              settlement_date=self.effective_date.isoformat(),
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
            # Call LUSID to upsert our transactions
            upsert_transactions_response = self.client.upsert_transactions(scope=self.internal_scope_code,
                                                                           code=portfolio_name,
                                                                           transactions=stock_in_transactions)

            # Tests - Verify that the transactions were added succesfully
            self.transactions_added_asserts(portfolio_scope=self.internal_scope_code,
                                            portfolio_code=portfolio_name,
                                            start_date=self.effective_date,
                                            end_date=self.effective_date,
                                            as_at_date=datetime.now(pytz.UTC).isoformat(),
                                            batch_transactions_request=stock_in_transactions)

    @timeit
    def create_strategy_tags(self):
        """
        This method handles the creation of our strategy tags. We use these to note what investment strategy we were
        following when we made a trade.

        In LUSID we do this using what is known as a property. A property is user defined in advance and can be set on
        any LUSID object. We are going to create a property called 'strategy' which will take the value of a string.
        We will attach this property to each transaction. The string will be the name of the strategy that we are
        following when making the transaction e.g. 'QuantitativeSignal' or 'FundamentalAnalysis'.

        Each property sits inside a domain. This domain tells us which LUSID objects we can attach the property
        to. In this case we want to attach our property to transactions so we use the 'Trade' domain. Other options
        are "Portfolio", "Security", "Holding", "ReferenceHolding", "TxnType", "Instrument" and "CutDefinition".

        When we set up a property we are required to give it a data type. We do this by specifying a data type using its
        ResourceId. This is the scope and code of the object. There are a number of pre-configured types in
        the default scope which we can draw from. We can also create our own types. In this case we will use the
        default string type.

        You can read more about defining new properties here: https://docs.lusid.com/#operation/CreatePropertyDefinition
        """
        # Create our request to define a new property
        property_request = models.CreatePropertyDefinitionRequest(domain='Trade',
                                                                  scope=self.internal_scope_code,
                                                                  code='strategy',
                                                                  value_required=False,
                                                                  display_name='strategy',
                                                                  data_type_id=models.ResourceId(scope='default',
                                                                                                 code='string'))
        # Call LUSID to create our new property
        property_response = self.client.create_property_definition(definition=property_request)

        # Grab the key off the response to use when referencing this property in other LUSID calls
        self.strategy_property_key = property_response.key

        # Test - Check that the property has been created successfully
        self.create_property_definition_asserts(property_request, property_response)

    @timeit
    def add_first_transactions(self):
        """
        This method upserts the first transactions we make for this client.

        Now that we have defined our strategy tag property for use on our transactions, we can make some trades
        for our new clients attaching the appropriate tag to each trade.
        """

        '''
        We had some exciting new strategies to implement for our new client across our portfolios that involved:

        1) Selling stock in Kingfisher
        2) Buying more of the UK Treasury Gilt maturing in 2034 with coupon rate of 4.5%
        3) Buying some more UK Treasury Gilts and selling US Treasury Bonds
        
        Let us define the trades below. Keeping in mind that these would be generated from our order management or
        execution management system in reality. Each trade has a unique identifier prefixed with tid_. It also has a
        transaction date and settlement date. 
        '''
        # Set the time of the start of the yesterday's trading day
        yesterday = datetime.now(pytz.UTC) - timedelta(days=1)
        t = time(hour=8, minute=0)
        self.yesterday_trade_open = pytz.utc.localize(datetime.combine(yesterday, t))
        # Create a list of hours we executed the trades at
        hours = [1, 5, 3, 4]

        self.client_transactions = {

            'client-{}-mandate-balanced'.format(self.client_id): {
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

            'client-{}-mandate-fixedincome'.format(self.client_id): {
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

        # Iterate over our portfolios
        for portfolio_name, transactions in self.client_transactions.items():
            # Initialise a list to hold our transactions for each portfolio
            batch_transaction_requests = []
            # Iterate over the transactions for each portfolio
            for transaction_id, transaction in transactions.items():
                # Append the transaction to our request, note the use of the 'properties' argument
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
            # Call LUSID to upsert our transactions
            transaction_response = self.client.upsert_transactions(scope=self.internal_scope_code,
                                                                   code=portfolio_name,
                                                                   transactions=batch_transaction_requests)

            # Test - Ensure that the transactions have been added correctly
            self.transactions_added_asserts(portfolio_scope=self.internal_scope_code,
                                            portfolio_code=portfolio_name,
                                            start_date=self.yesterday_trade_open.isoformat(),
                                            end_date=(self.yesterday_trade_open + timedelta(
                                                days=max(hours))).isoformat(),
                                            as_at_date=datetime.now(pytz.UTC).isoformat(),
                                            batch_transactions_request=batch_transaction_requests)

            # Tests - Ensure that the transactions have the new strategy property attached to them
            for transaction in batch_transaction_requests:
                self.add_transaction_property_asserts(self.internal_scope_code,
                                                      portfolio_name,
                                                      transaction.transaction_id,
                                                      self.strategy_property_key,
                                                      transaction.properties[self.strategy_property_key].label_value)

    @timeit
    def create_analytics(self):
        """
        This method creates an analytics store which is required to run aggregation requests. You can read more
        about creating an analytics store here: https://docs.lusid.com/#operation/CreateAnalyticStore
        """
        # Set our analytics effective date to be from now
        analytics_effective_date = datetime.now(pytz.UTC)

        # Create analytics store request
        analytics_store_request = models.CreateAnalyticStoreRequest(scope=self.internal_scope_code,
                                                                    date_property=analytics_effective_date.isoformat())
        # Call LUSID to create our analytics store
        self.client.create_analytic_store(request=analytics_store_request)

        # Create prices via instrument, analytic
        instrument_analytics = []

        # Create dummy prices of 1 for all instruments except cash
        for instrument_name, instrument in self.instrument_universe.items():
            if 'Cash' in instrument_name:
                continue
            instrument_analytics.append(models.InstrumentAnalytic(instrument_uid=instrument['identifiers']['LUID'],
                                                                  value=1))

        # Call LUSID to set up our newly created analytics store
        self.client.set_analytics(scope=self.internal_scope_code,
                                  year=analytics_effective_date.year,
                                  month=analytics_effective_date.month,
                                  day=analytics_effective_date.day,
                                  data=instrument_analytics)

    @timeit
    def aggregate_portfolio_group(self):
        """
        This method is used to aggregate all of our client's portfolios by aggregating across their portfolio group.

        You can read more about aggregation by portfolio group here:
        https://docs.lusid.com/#operation/GetAggregationByGroup
        """
        # Create our aggregation request
        aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                    code='default'),
                                                        effective_at=datetime.now(pytz.UTC).isoformat(),
                                                        metrics=[
                                                            models.AggregateSpec(key='Holding/default/SubHoldingKey',
                                                                                 op='Value'),
                                                            models.AggregateSpec(key='Holding/default/Units',
                                                                                 op='sum'),
                                                            models.AggregateSpec(key='Holding/default/Cost',
                                                                                 op='sum')
                                                            ])

        # Call LUSID to aggregate across all of our portfolios
        aggregated_group = self.client.get_aggregation_by_group(scope=self.internal_scope_code,
                                                                code=self.client_portfolio_group_code,
                                                                request=aggregation_request)

        # Test - Confirm the aggregation result is correct
        self.verify_portfolio_group_aggregation_asserts(aggregated_response=aggregated_group,
                                                        portfolio_group_scope=self.internal_scope_code,
                                                        portfolio_group_code=self.client_portfolio_group_code,
                                                        effective_at=datetime.now(pytz.UTC).isoformat())

    @timeit
    def aggregate_strategy(self):
        """
        This method is used to aggregate by strategy across all of our client's portfolios by aggregating across
        their portfolio group and grouping as well as filtering by our strategy tags.
        """

        # Let us create a new scope for our strategy aggregation. This is because we need to create derived portfolios
        self.strategy_scope = 'strategy-scope-{}'.format(uuid.uuid4())

        '''
        To aggregate by strategy we need to pass the strategy label that we have added to our transactions into our
        holdings. The way to do this is through what are known as 'sub-holding keys' a sub-holding key is a way to group
        transactions into separate holdings based on a given property.
        
        For example if we have 5 transactions on a security labelled with a strategy property of 'quantitativeSignal' 
        and 3 transactions with a strategy property of 'fundamentalAnalysis' these will by default be grouped together
        and our portfolio will show the net holdings of all 8 transactions added together. If we use the strategy
        property as a sub-holding key, the 5 transactions labelled 'quantitativeSignal' will be grouped together as will
        the 3 transactions labelled 'fundamentalAnalysis'. This gives us two holdings for the same security, separated
        by the strategy followed.
        
        To create sub-holding keys we need to use what is known as a 'Derived Portfolio'. A derived portfolio is a
        portfolio that inherits all of its transactions and thus holdings from a parent portfolio. When we create the
        derived portfolio we specify which properties we would like to use for our sub-holding keys. 
        
        We will create a derived portfolio for each of our client's portfolios. 
                
        We will use the same code for our derived portfolios as we do for our parent portfolios, for this reason we
        need to create them in a separate scope so that we don't have any naming collisions. 
        
        You can read more about creating derived portfolios here: 
        https://docs.lusid.com/#operation/CreateDerivedPortfolio
        '''
        # Initialise our list of derived portfolios so that we can group them
        derived_portfolio_resourceids = []
        # Loop through each of our portfolios
        for portfolio_code in self.client_portfolios:
            # Create the request to create our derived portfolio
            portfolio_request = models.CreateDerivedTransactionPortfolioRequest(display_name=portfolio_code,
                                                                                code=portfolio_code,
                                                                                parent_portfolio_id=models.ResourceId(
                                                                                    scope=self.internal_scope_code,
                                                                                    code=portfolio_code),
                                                                                description=portfolio_code,
                                                                                created=self.created_date,
                                                                                sub_holding_keys=[
                                                                                    self.strategy_property_key])
            # Call LUSID to create our derived portfolio
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
            derived_portfolio_resourceids.append(models.ResourceId(scope=self.strategy_scope, code=portfolio_code))

        # Create our portfolio group request
        portfolio_group_request = models.CreatePortfolioGroupRequest(id=self.client_portfolio_group_code,
                                                                     display_name=self.client_portfolio_group_code,
                                                                     values=derived_portfolio_resourceids,
                                                                     description='Grouping all of client {} portfolios'
                                                                     .format(self.client_id))
        # Call LUSID to create our portfolio group
        portfolio_group = self.client.create_portfolio_group(scope=self.strategy_scope,
                                                             request=portfolio_group_request)

        # Tests - Ensure that we have successfully created the portfolio group
        self.portfolio_group_creation_asserts(portfolio_group, portfolio_group_request, self.strategy_scope)

        # Create our aggregation request, note the use of the group_by and filters arguments
        aggregation_request = models.AggregationRequest(recipe_id=models.ResourceId(scope=self.internal_scope_code,
                                                                                    code='default'),
                                                        effective_at=datetime.now(pytz.UTC).isoformat(),
                                                        metrics=[models.AggregateSpec(key='Holding/default/Units',
                                                                                      op='sum'),
                                                                 models.AggregateSpec(key='Holding/default/Cost',
                                                                                      op='sum')],
                                                        group_by=[self.strategy_property_key,
                                                                  'Instrument/default/Name'],
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

        # Call LUSID to get our aggregated group
        aggregated_group = self.client.get_aggregation_by_group(scope=self.strategy_scope,
                                                                code=self.client_portfolio_group_code,
                                                                request=aggregation_request)

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
