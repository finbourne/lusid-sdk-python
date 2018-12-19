import unittest
import uuid
import lusid.models as models
import pytz
from datetime import datetime, timedelta
from finbournetest import TestFinbourneApi

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class businessAgilityTestEnvironment(TestFinbourneApi):

    def import_data(self):
        '''
        We are an asset manager who has recently secured a contract to work with a new small pension fund. The pension
        fund has decided to switch from their incumbent asset manager on the advice of consultants. The transition
        is being handled by a transition manager and we have just received the transition accounts with the final
        confirmed holdings that we will make up the initial portfolio for the fund.

        As part of the investment agreement with the pension fund they would like to make some changes to the way
        that they receive their reporting. They would also like to start investing in some exotic over the counter
        instruments which our internal systems do not support. Therefore in addition to setting up a production
        portfolio with the initial holdings, we will also need to create a test environment to model these changes
        without affecting the live environment.

        Furthermore, we are also about to go through a larger audit process. As part of this process we need to ensure
        that the correct entitlements are set up on the production and test environments and portfolios so that only
        the fund managers for the new client can access the live portfolio and only the development team working on
        building the modified reporting and adding support for the exotic instruments can access the development
        portfolio.
        '''

        '''
        In LUSID we can create separate environments using Scopes. A Scope is a container which acts as a separate
        namespace. This allows us to have a portfolio with the same code in different scopes without having to
        worry about collisions
        '''

        # Create a unique id for our client to use in the production and test scopes
        scope_id = uuid.uuid4()
        # Using the id create a unique code for each scope, this is what identifies the scope
        self.production_scope_code = 'production-client-{}'.format(scope_id)
        self.test_scope_code = 'test-client-{}'.format(scope_id)
        # Also create a code for our portfolio, we will re-use the same code in each scope
        portfolio_id = uuid.uuid4()
        self.portfolio_code = 'pension-fund-{}'.format(portfolio_id)

        # The official transfer time is 12 hours from now, note that in LUSID the datetime must be in ISO8601 format
        self.official_transfer_time = (datetime.now(pytz.UTC) + timedelta(hours=12)).isoformat()

        '''
        These are the initial holdings we are taking on from the fund, we have 10 instruments which have been 
        transferred to us. This data may have been imported from a spreadsheet, fetched by and API etc.

        It could be in a range of formats such as in a list, a dictionary, a pandas DataFrame etc.

        In this case we are using a simple dictionary using the name of the instrument as the key. Each instrument 
        has an initial quantity, price, currency and internal client ID. 
        '''

        self.transferred_instruments = {
            'WPP_LondonStockEx_WPP': {
                'identifiers': {'ClientInternal': 'Isin-JE00B8KF9B49'},
                'quantity': 1050200,
                'price': 8.7100,
                'currency': 'GBP'},

            'UKGiltTreasury_3.5_2045': {
                'identifiers': {'ClientInternal': 'Isin-GB00BN65R313'},
                'quantity': 100674,
                'price': 129.976,
                'currency': 'GBP'},

            'UKGiltTreasury_2.0_2025': {
                'identifiers': {'ClientInternal': 'Isin-GB00BTHH2R79'},
                'quantity': 220456,
                'price': 106.421,
                'currency': 'GBP'},

            'UKGiltTreasury_4.5_2034': {
                'identifiers': {'ClientInternal': 'Isin-GB00B52WS153'},
                'quantity': 97658,
                'price': 138.466,
                'currency': 'GBP'},

            'UKGiltTreasury_3.75_2021': {
                'identifiers': {'ClientInternal': 'Isin-GB00B4RMG977'},
                'quantity': 320568,
                'price': 108.175,
                'currency': 'GBP'},

            'Kingfisher_LondonStockEx_KGF': {
                'identifiers': {'ClientInternal': 'Isin-GB0033195214'},
                'quantity': 2879200,
                'price': 2.3940,
                'currency': 'GBP'},

            'JustEat_LondonStockEx_JE': {
                'identifiers': {'ClientInternal': 'Isin-GB00BKX5CN86'},
                'quantity': 4789100,
                'price': 5.9780,
                'currency': 'GBP'},

            'RELXGroup_LondonStockEx_REL': {
                'identifiers': {'ClientInternal': 'Isin-GB00B2B0DG97'},
                'quantity': 6134800,
                'price': 16.5750,
                'currency': 'GBP'},

            'TESCO_LondonStockEx_TSCO': {
                'identifiers': {'ClientInternal': 'Isin-GB0008847096'},
                'quantity': 13456500,
                'price': 1.9365,
                'currency': 'GBP'},

            'Whitebread_LondonStockEx_WTB': {
                'identifiers': {'ClientInternal': 'Isin-GB00B1KJJ408'},
                'quantity': 8954300,
                'price': 4.56900,
                'currency': 'GBP'}
        }

    def create_portfolio_production_environment(self):
        '''
        The first thing that we need to do is create a production environment with an empty transaction portfolio which
        we can use to hold the assets of the pension fund.
        We will test that the production environment and pension fund portfolio are created successfully
        '''

        # Create our pension fund portfolio in the production scope
        pension_fund_request = models.CreateTransactionPortfolioRequest(display_name='pension-fund',
                                                                        code=self.portfolio_code,
                                                                        base_currency='GBP',
                                                                        description='Pension fund for new client')

        pension_fund_portfolio = self.client.create_portfolio(scope=self.production_scope_code,
                                                              create_request=pension_fund_request)

        # Test that our portfolio was created successfully
        self.portfolio_creation_tests(pension_fund_portfolio, pension_fund_request, self.production_scope_code)

    def add_holdings_portfolio_production_environment(self):
        '''
        Now that we have created our portfolio in the production environemnt, we need to take the final holdings report
        that we received from the transition manager and populate our portfolio.
        Before we do this, we first need to do add the instruments to LUSID. Once we have added the instruments we can
        then populate our initial holdings on these instruments.
        We will test that we have correctly created the instruments and added the holdings to our portfolio
        '''

        '''
        Rather than using separate update and insert methods, LUSID uses an upsert method for may of its operations.

        This inserts a record if it does not already exist and modifies an existing record if it does already exist.

        We can upsert our instruments individually or in a batch. Either way the request should be in the form of a
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
        # Initialise our batch upsert request
        batch_upsert_request = {}
        # Using then initial holdings information, create our batch
        for instrument_name in self.transferred_instruments:
            batch_upsert_request[instrument_name] = models.UpsertInstrumentRequest(name=instrument_name,
                                                                                   identifiers=
                                                                                   self.transferred_instruments[
                                                                                       instrument_name]['identifiers'])
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
            # Loop over our transferred instruments looking for the right match
            for instrument_name, transferred_instrument in self.transferred_instruments.items():
                # If the identifiers match
                if transferred_instrument['identifiers']['ClientInternal'] == instrument.identifiers['ClientInternal']:
                    # Add our LUID as a new identifier so that we can use it in our calls later
                    transferred_instrument['identifiers']['LUID'] = instrument.lusid_instrument_id

        '''
        Now that we have our instruments added we can create transactions to fill our initial holdings.

        As we have just received the assets from the transition manager we are unsure of the purchase dates of each
        lot of assets over their history. All we know is that we have a given quantity today at a given price agreed 
        upon with the transition manager

        To set our holdings we use a list of AdjustHoldingRequest objects.

        The AdjustHoldingRequest object has a number of fields these are:
            - instrument_uid: This is the LUID of the instrument we want to adjust the holdings for
            - tax_lots: This is a list of tax lots. A tax lot being instruments purchased at different times and thus needing
                        different treatment for tax purposes. In this case as we are only given the current holding information
                        from the transition manager we only need to use a single tax lot
                - units: This is the quantity of the instrument that we are holding
                - cost: This is the total cost of the instrument and the currency it is in
                    - amount: The total cost/value of the instrument, here we multiply the instrument's price by its
                              quantity to get the total amount
                    - currency: The currency that the instrument is in as a string, must be tk - what currencies are allowed??
                - portfolio_cost: This is the total cost of the instrument in the portfolio's currency
                - price: This is the price if the instrument tk - in what currency???? Is this in the portfolio currency?
        '''

        # Initialise our holding adjustments list
        holding_adjustments = []

        # Create a holding adjustment for each instrument using the information given to use by the transition manager
        for instrument_name, instrument in self.transferred_instruments.items():
            holding_adjustments.append(
                models.AdjustHoldingRequest(instrument_uid=instrument['identifiers']['LUID'],
                                            tax_lots=[
                                                models.TargetTaxLotRequest(units=instrument['quantity'],
                                                                           cost=models.CurrencyAndAmount(
                                                                               amount=instrument['quantity'] *
                                                                                      instrument['price'],
                                                                               currency=instrument['currency']),
                                                                           portfolio_cost=instrument['quantity'] *
                                                                                          instrument['price'],
                                                                           price=instrument['price'])
                                            ]
                                            )
            )

        '''
        Now that we have built our list of holding adjustments we want to update the portfolio with them.

        Note that when we do this we need to specify an effective date for the holdings. This date is the date from 
        which the holdings are valid. In this case the date will be the official date of the transition of the funds to 
        us. 

        Note that our portfolio also has an effective date from which it is active. This was created automatically when
        we created our portfolio. The effecitve date of our holdings must be after the effective date of the portfolio. 

        The reason for this is that LUSID is built upon a bi-temporal data store. The implications of this are that 
        every object has two dates attached to it. These are the effective at date and the as at date. 

        The as at date defines the date at which an object was added to the system. For example in the portfolio we 
        just created the as at date is today.

        The effective at date defines the date from which an object should be valid. For example if we set our 
        portfolio's effective date to be the 1st of January 2018, it will be valid from that date and we can add
        any transactions to it from that date onwards. We cannot add holdings or transactions to this portfolio before 
        this date as the portfolio did not exist and as such there is nothing for the holdings to be attached to. 

        This bi-temporal store gives us the ability to look re-create how our system looks at any point in time. For
        example if we look at the state of our system using an as at date of 2 days before today and thus 2 days before
        our portfolio was created, we will not be able to find our portfolio as it had not been created in the system at
        that point in time. 
        '''

        # Set our holdings on our production portfolio
        holdings = self.client.set_holdings(scope=self.production_scope_code,
                                            code=self.portfolio_code,
                                            effective_at=self.official_transfer_time,
                                            holding_adjustments=holding_adjustments)

        # Test to verify that the holdings have been set
        self.verify_holdings_tests(holding_adjustments=holding_adjustments,
                                   holdings=holdings,
                                   scope=self.production_scope_code,
                                   code=self.portfolio_code,
                                   effective_at=self.official_transfer_time)

    def create_derived_portfolio_test_environment(self):
        '''
        Now that we have loaded the holdings into our production environment we need to create a test environment to
        model the changes that the pension fund has requested without affecting our day to day operations.
        This is especially important as they are a new client and we don't want to cause any problems so early into the
        transition by causing problems in production.
        We therefore want to be able to create a replica of our pension portfolio in the test environment so we can
        clearly see how the changes would affect us as if they were in a live environment. To do this we will create a
        derived portfolio.
        A derived portfolio can be thought of as a child portfolio. It inherits properties, transactions and holdings
        from a parent portfolio.
        In this case we will create a derived portfolio from our pension portfolio in the production environment. Any
        changes to the production portfolio will be replicated to the test portfolio.
        We will test that we have succesfully created a test environment and derived portfolio which is a mirror image
        of our production pension portfolio
        '''

        '''
        Create our derived pension fund portfolio in the test scope, we use the same code for the portfolio as in the
        production scope. Recall that each scope is a separate namespace allowing us to use the same names in different
        scopes. 
        '''
        derived_pension_fund_request = models.CreateDerivedTransactionPortfolioRequest(display_name='pension-fund',
                                                                                       code=self.portfolio_code,
                                                                                       description='Pension fund for new client',
                                                                                       parent_portfolio_id=models.ResourceId(
                                                                                           scope=self.production_scope_code,
                                                                                           code=self.portfolio_code)
                                                                                       )

        derived_pension_fund_portfolio = self.client.create_derived_portfolio(scope=self.test_scope_code,
                                                                              portfolio=derived_pension_fund_request)

        # Test that our derived portfolio has been created successfully
        self.derived_portfolio_creation_tests(derived_pension_fund_portfolio, derived_pension_fund_request,
                                              self.test_scope_code)
        # Test that it has the same holdings as the parent
        self.reconcile_portfolios_tests(portfolio_left_scope=self.production_scope_code,
                                        portfolio_left_code=self.portfolio_code,
                                        portfolio_left_effective_date=self.official_transfer_time,
                                        portfolio_left_as_at=datetime.now(pytz.UTC).isoformat(),
                                        portfolio_right_scope=self.test_scope_code,
                                        portfolio_right_code=self.portfolio_code,
                                        portfolio_right_effective_date=self.official_transfer_time,
                                        portfolio_right_as_at=datetime.now(pytz.UTC).isoformat(),
                                        check_same=True)

    def add_more_transactions_portfolio_production_environment(self):
        '''
        Now that we have the client's funds we are on the clock and need to ensure we are driving superior performance
        compared with their last manager. To do this we have made some transactions to optimise performance. We now need
        to update our production pension portfolio with these transactions.
        In this case we will use synthetic transactions, however in practice these will likely be fed in from an order
        manage system or execution management system.
        This test will ensure that we have successfully added our transactions to the production pension portfolio and
        the holdings have been update appropriately. We will also test that these changes have been replicated to our
        derived portfolio in the test environment
        '''

        '''
        We can add transactions individually or in batches using a list of TransactionRequest objects.

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

        To optimise performance we have made 5 trades so far that we need to add. Once again in reality these trades
        would be fed through from the order management or execution management system.

        1) We sold 410,000 WPP shares on the back of the effects of GDPR on the advertising industry
        2) We bought 70,000 ULVR (Unilever) shares on the prediction of a quantitative model
        3) We sold all our KGF (Kingfisher) shares on the back of a strong analysts pessimistic forecast for home improvement
        4) We bought 180,000 shares in ABF (Associated Bristish Foods) to get more exposure to retail after the sale of the Kingfisher shares
        5) We bought 669,180 shares in GLEN (Glencore) based on fundamental analysis revealing it to be under priced off the back of recent negative news about the company
        '''

        '''
        The first thing that we need to do is add our new instruments to Lusid
        '''

        # Add Glencore, Uniliver and Associated British Food Instruments
        self.new_instruments = {
            'Unilever_LondonStockEx_ULVR': {
                'identifiers': {'ClientInternal': 'Isin-GB00B10RZP78'},
                'currency': 'GBP'},

            'ABFood_LondonStockEx_ABF': {
                'identifiers': {'ClientInternal': 'Isin-GB0006731235'},
                'currency': 'GBP'},

            'Glencore_LondonStockEx_GLEN': {
                'identifiers': {'ClientInternal': 'Isin-JE00B4T3BW64'},
                'currency': 'GBP'},
        }
        # Initialise our upsert request
        batch_upsert_request = {}
        # Create our batch which has the instrument name as the key for each instrument
        for instrument_name in self.new_instruments:
            batch_upsert_request[instrument_name] = models.UpsertInstrumentRequest(name=instrument_name,
                                                                                   identifiers=
                                                                                   self.new_instruments[
                                                                                       instrument_name]['identifiers'])
        # Upsert our batch
        batch_upsert_response = self.client.upsert_instruments(requests=batch_upsert_request)

        # Tests - Confirm that the response is as expected
        self.instrument_upsert_tests(batch_upsert_response, batch_upsert_request)

        # Add our newly created lusid_instrument_id or LUID for short to our new instruments dictionary
        for result, instrument in batch_upsert_response.values.items():
            # Loop over our instruments looking for the correct one
            for instrument_name, new_instrument in self.new_instruments.items():
                # If the identifiers match
                if new_instrument['identifiers']['ClientInternal'] == instrument.identifiers['ClientInternal']:
                    # Add our LUID as a new identifier so that we can use it in our calls later
                    new_instrument['identifiers']['LUID'] = instrument.lusid_instrument_id

        '''
        Now that we've added our new instruments, let's define our transactions. For each transaction we will
        generate a unique id and prefix it with 'tid_'. These will be our convention for naming transactions. 

        In reality this information would likely be populated via our order management or execution management system.
        '''

        transactions = {
            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Sell',
                'instrument_uid': self.transferred_instruments['WPP_LondonStockEx_WPP']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=2)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=3)).isoformat(),
                'units': 410000,
                'transaction_price': 8.3720,
                'transaction_currency': 'GBP',
            },

            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Buy',
                'instrument_uid': self.new_instruments['Unilever_LondonStockEx_ULVR']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=2)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=3)).isoformat(),
                'units': 70000,
                'transaction_price': 42.3250,
                'transaction_currency': 'GBP',
            },

            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Sell',
                'instrument_uid': self.transferred_instruments['Kingfisher_LondonStockEx_KGF']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=2)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=3)).isoformat(),
                'units': 2879200,
                'transaction_price': 2.3630,
                'transaction_currency': 'GBP',
            },

            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Buy',
                'instrument_uid': self.new_instruments['ABFood_LondonStockEx_ABF']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=2)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=4)).isoformat(),
                'units': 180000,
                'transaction_price': 23.7400,
                'transaction_currency': 'GBP',
            },

            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Buy',
                'instrument_uid': self.new_instruments['Glencore_LondonStockEx_GLEN']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=3)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=5)).isoformat(),
                'units': 669180,
                'transaction_price': 2.7385,
                'transaction_currency': 'GBP',
            }
        }

        '''
        Now that we have the data for our transactions we can great our batch transactions request. In this case
        we use a list to hold our transactions rather than a dictionary
        '''
        # Initialise our batch
        batch_transactions_request = []
        # Create our batch
        for transaction_id, transaction in transactions.items():
            batch_transactions_request.append(
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

        # Upsert our batch of transactions
        portfolio_transactions = self.client.upsert_transactions(scope=self.production_scope_code,
                                                                 code=self.portfolio_code,
                                                                 transactions=batch_transactions_request)

        # Test that transactions were all added
        self.transactions_added_tests(portfolio_scope=self.production_scope_code,
                                      portfolio_code=self.portfolio_code,
                                      start_date=(datetime.now(pytz.UTC) + timedelta(days=1)).isoformat(),
                                      end_date=(datetime.now(pytz.UTC) + timedelta(days=5)).isoformat(),
                                      as_at_date=datetime.now(pytz.UTC).isoformat(),
                                      batch_transactions_request=batch_transactions_request)

        # Test to check that the derived portfolio inherited the transactions
        last_settlement_date = (datetime.now(pytz.UTC) + timedelta(days=5)).isoformat()
        self.reconcile_portfolios_tests(portfolio_left_scope=self.production_scope_code,
                                        portfolio_left_code=self.portfolio_code,
                                        portfolio_left_effective_date=last_settlement_date,
                                        portfolio_left_as_at=datetime.now(pytz.UTC).isoformat(),
                                        portfolio_right_scope=self.test_scope_code,
                                        portfolio_right_code=self.portfolio_code,
                                        portfolio_right_effective_date=last_settlement_date,
                                        portfolio_right_as_at=datetime.now(pytz.UTC).isoformat(),
                                        check_same=True)

    def add_transactions_derived_portfolio_test_environment(self):
        '''
        We also want to add some synthetic transactions to our test pension portfolio to test some edge cases that may
        arise from our changes. Let us add these in.
        We will just make two transactions in existing instruments.
        1) Sell 50,000 Associated British Foods Shares
        2) Buy 100,000 Glencore Shares
        This test will ensure that we have successfully added our transactions to the test pension portfolio which is
        derived from the production environment. We will also ensure that none of these changes have been replicated
        back to production and that they are isolated to our test environment.
        '''

        transactions = {
            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Sell',
                'instrument_uid': self.new_instruments['ABFood_LondonStockEx_ABF']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=6)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=8)).isoformat(),
                'units': 50000,
                'transaction_price': 23.4500,
                'transaction_currency': 'GBP',
            },

            'tid_{}'.format(uuid.uuid4()): {
                'type': 'Buy',
                'instrument_uid': self.new_instruments['Glencore_LondonStockEx_GLEN']['identifiers']['LUID'],
                'transaction_date': (datetime.now(pytz.UTC) + timedelta(days=6)).isoformat(),
                'settlement_date': (datetime.now(pytz.UTC) + timedelta(days=8)).isoformat(),
                'units': 100000,
                'transaction_price': 2.7385,
                'transaction_currency': 'GBP',
            }
        }

        '''
        Now that we have the data for our transactions we can great our batch transactions request
        '''
        # Initialise batch transactions request
        batch_transactions_request = []

        for transaction_id, transaction in transactions.items():
            batch_transactions_request.append(
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

        # Upsert our transactions, note that we have changed the scope here to our test scope
        portfolio_transactions = self.client.upsert_transactions(scope=self.test_scope_code,
                                                                 code=self.portfolio_code,
                                                                 transactions=batch_transactions_request)

        # Test that transactions were all added
        self.transactions_added_tests(portfolio_scope=self.test_scope_code,
                                      portfolio_code=self.portfolio_code,
                                      start_date=(datetime.now(pytz.UTC) + timedelta(days=5)).isoformat(),
                                      end_date=(datetime.now(pytz.UTC) + timedelta(days=8)).isoformat(),
                                      as_at_date=datetime.now(pytz.UTC).isoformat(),
                                      batch_transactions_request=batch_transactions_request)

        # Test to check that the production portfolio was not affected
        last_settlement_date = (datetime.now(pytz.UTC) + timedelta(days=8)).isoformat()
        self.reconcile_portfolios_tests(portfolio_left_scope=self.production_scope_code,
                                        portfolio_left_code=self.portfolio_code,
                                        portfolio_left_effective_date=last_settlement_date,
                                        portfolio_left_as_at=datetime.now(pytz.UTC).isoformat(),
                                        portfolio_right_scope=self.test_scope_code,
                                        portfolio_right_code=self.portfolio_code,
                                        portfolio_right_effective_date=last_settlement_date,
                                        portfolio_right_as_at=datetime.now(pytz.UTC).isoformat(),
                                        transactions=batch_transactions_request,
                                        check_same=False)

    def create_entitlements(self):
        '''
        We are undergoing an audit and need to ensure that the right people have access to the right portfolios. We
        currently use a number of protections but want to ensure we are covered at every level. We will set up
        entitlements on the production pension portfolio to ensure that only the investment managers have access. We will
        also set up entitlements on the test pension portfolio to ensure that only the development team working on the
        project have access.
        This test will ensure that we have correctly provisioned entitlements and that they are working correctly.
        '''

    def test_business_agility(self):
        self.import_data()
        self.create_portfolio_production_environment()
        self.add_holdings_portfolio_production_environment()
        self.create_derived_portfolio_test_environment()
        self.add_more_transactions_portfolio_production_environment()
        self.add_transactions_derived_portfolio_test_environment()
        self.create_entitlements()


if __name__ == '__main__':
    unittest.main()