import unittest
from functools import reduce
from timeit import default_timer as timer
from unittest import TestCase

import lusid
import lusid.models as models
from api_client_builder import ApiClientBuilder

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


def timeit(func):
    """
    This function is used as a decarator i.e. @timeit for a function to time how
    long it takes to run
    """

    def timed(*args, **kwargs):
        # start timer
        start = timer()
        # run function
        result = func(*args, **kwargs)
        # end timer
        end = timer()
        # print the time taken to run the function
        print(func.__name__, ' took ', end - start, ' seconds to execute')
        return result

    return timed


class TestFinbourneApi(TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        """
        Here we handle authentication. We use a username, password, client ID and client secret to authenticate
        our account.
        """
        api_client = ApiClientBuilder().build("secrets.json")

        # set up the APIs
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.property_definition_api = lusid.PropertyDefinitionsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.analytic_stores_api = lusid.AnalyticsStoresApi(api_client)
        cls.aggregation_api = lusid.AggregationApi(api_client)
        cls.derived_transaction_portfolio_api = lusid.DerivedTransactionPortfoliosApi(api_client)
        cls.reconciliations_api = lusid.ReconciliationsApi(api_client)
        cls.portfolio_groups_api = lusid.PortfolioGroupsApi(api_client)

    def portfolio_creation_asserts(self, portfolio, portfolio_request, scope):
        """
        This method contains a set of assertions used to test the successful creation of a portfolio, we test that:
        - No error is returned
        - The portfolio is created with the correct code
        - The portfolio is created within the correct scope
        - The portfolio is created with the correct display name
        - The portfolio is created with the correct description
        """

        self.assertNotIsInstance(portfolio, models.ErrorResponse, 'No portfolio created, error returned')
        self.assertEqual(portfolio_request.code, portfolio.id.code,
                         'Portfolio created with code {} instead of code {}'.format(portfolio.id.code,
                                                                                    portfolio_request.code))
        self.assertEqual(scope, portfolio.id.scope,
                         'Portfolio created in scope {} instead of scope {}'.format(portfolio.id.scope,
                                                                                    scope))
        self.assertEqual(portfolio_request.display_name, portfolio.display_name,
                         'Portfolio created with name {} instead of {}'.format(portfolio.display_name,
                                                                               portfolio_request.display_name))
        self.assertEqual(portfolio_request.description, portfolio.description,
                         'Portfolio created with description {} instead of {}'.format(
                             portfolio.description,
                             portfolio_request.description))

    def portfolio_group_creation_asserts(self, portfolio_group, portfolio_group_request, group_scope):
        """
        This method contains a set of tests used to test the successful creation of a portfolio group, we test that:
        - No error is returned
        - The portfolio group is created with the correct code
        - The portfolio group is created within the correct scope
        - The portfolio group is created with the correct display name
        - The portfolio group is created with the correct description
        - The portfolio group is created with the right number of portfolios
        """

        self.assertNotIsInstance(portfolio_group, models.ErrorResponse,
                                 'Portfolio group not created, error returned')

        self.assertEqual(portfolio_group.id.code, portfolio_group_request.id,
                         'Portfolio group code is {} instead of {}'.format(portfolio_group.id.code,
                                                                           portfolio_group_request.id))

        self.assertEqual(portfolio_group.id.scope, group_scope,
                         'Portfolio group scope is {} instead of {}'.format(portfolio_group.id.scope,
                                                                            group_scope))

        self.assertEqual(portfolio_group.display_name, portfolio_group_request.display_name,
                         'Portfolio group display name is {} instead of {}'.format(portfolio_group.display_name,
                                                                                   portfolio_group_request.display_name))

        self.assertEqual(portfolio_group.description, portfolio_group_request.description,
                         'Portfolio group description is {} instead of {}'.format(portfolio_group.description,
                                                                                  portfolio_group_request.description))

        self.assertEqual(len(portfolio_group.portfolios), len(portfolio_group_request.values),
                         'Portfolio group has {} portfolios instead of {}'.format(portfolio_group.description,
                                                                                  portfolio_group_request.description))

        '''
        Iterate over the portfolios checking that the scope and code is correct. Note that this currently does not
        support the case where none or less than all of the portfolios match. All it handles is if the code matches
        so does the scope. 
        '''

        portfolio_requests = {request.code: request for request in portfolio_group_request.values}

        # Iterate over the portfolios in our group
        for portfolio in portfolio_group.portfolios:
            portfolio_request = portfolio_requests[portfolio.code]
            self.assertEqual(portfolio.scope, portfolio_request.scope,
                             'Portfolio {} has scope {} instead of {}'.format(portfolio.code,
                                                                              portfolio.scope,
                                                                              portfolio_request.scope))

    def derived_portfolio_creation_asserts(self, derived_portfolio, derived_portfolio_request, derived_portfolio_scope):
        """
        This method contains a set of tests used to test the successful creation of a derived portfolio, we test that:
        - The derived portfolio has its derived property set to True
        - The derived portfolio has the correct code
        - The derived portfolio has been created in the correct scope
        - The derived portfolio has been created with the correct display name
        - The derived portfolio has been created with the correct description
        - The derived portfolio has been created from the portfolio located in correct scope
        - The derived portfolio has been created from the portfolio with the correct code
        """

        self.assertEqual(derived_portfolio.is_derived, True,
                         'Expected derived portfolio to be True instead it is {}'.format(derived_portfolio.is_derived))

        self.assertEqual(derived_portfolio_request.code, derived_portfolio.id.code,
                         'Portfolio created with code {} instead of code {}'.format(derived_portfolio.id.code,
                                                                                    derived_portfolio_request.code))

        self.assertEqual(derived_portfolio_scope, derived_portfolio.id.scope,
                         'Portfolio created in scope {} instead of scope {}'.format(derived_portfolio.id.scope,
                                                                                    derived_portfolio_scope))

        self.assertEqual(derived_portfolio_request.display_name, derived_portfolio.display_name,
                         'Portfolio created with name {} instead of {}'.format(derived_portfolio.display_name,
                                                                               derived_portfolio_request.display_name))

        self.assertEqual(derived_portfolio_request.description, derived_portfolio.description,
                         'Portfolio created with description {} instead of {}'.format(
                             derived_portfolio.description,
                             derived_portfolio_request.description))

        self.assertEqual(derived_portfolio_request.parent_portfolio_id.scope,
                         derived_portfolio.parent_portfolio_id.scope,
                         'Portfolio created from portfolio in scope {} instead of {}'.format(
                             derived_portfolio.parent_portfolio_id.scope,
                             derived_portfolio_request.parent_portfolio_id.scope))

        self.assertEqual(derived_portfolio_request.parent_portfolio_id.code,
                         derived_portfolio.parent_portfolio_id.code,
                         'Portfolio created from portfolio with code {} instead of {}'.format(
                             derived_portfolio.parent_portfolio_id.code,
                             derived_portfolio_request.parent_portfolio_id.code))

    def instrument_upsert_asserts(self, batch_upsert_response, batch_upsert_request):
        """
        This method contains a set of tests used to test the successful upsert of instruments, we test that:
        - No instrument upserts failed
        - All instruments were successfully upserted
        - The instrument has a Lusid Instrument ID or LUID for short
        - The instrument name is in the request
        - The instrument identifiers match those in the request
        """

        # Confirm that the response is as expected
        self.assertLess(len(batch_upsert_response.failed), 1,
                        '{} upsert requests of {} failed'.format(len(batch_upsert_response.failed),
                                                                 len(batch_upsert_request)))

        self.assertEqual(len(batch_upsert_response.values), len(batch_upsert_request),
                         'Only {} upsert requests of {} successfully upserted'.format(
                             len(batch_upsert_request),
                             len(batch_upsert_response.values)))

        for result, instrument in batch_upsert_response.values.items():
            self.assertIsNotNone(instrument.lusid_instrument_id,
                                 'Instrument does not have a LUSID Instrument ID')

            self.assertIn(instrument.name, list(batch_upsert_request.keys()),
                          'The instrument name {} is not in those in the request {}'.format(
                              instrument.name,
                              batch_upsert_request.keys()))

            self.assertEqual(instrument.identifiers, batch_upsert_request[instrument.name].identifiers,
                             'The instrument has mismatched identifiers to the request')

    def verify_holdings_asserts(self, holding_adjustments, holdings, scope, code, effective_at):
        """
        This method contains a set of tests used to test that set holdings has worked correctly, we test that:
        - The holdings response contains links to the created resources
        - The number holdings matches the number of adjustments that we have made
        - The number of units in an upserted holding matches the request for a given instrument
        - The cost of an upserted holding matches the cost in the request for a given instrument
        - The currency of an upserted holding matches the currency in the request for a given instrument

        Note that for this test we are making the following assumptions:
        - We have only upsert a single tax lot for each holding
        - We have only upsert one holding adjustment for each instrument
        """

        self.assertIsNotNone(holdings.href, 'No hyperlink to holdings returned')

        # As we only get links back from our set holdings method, we need to retrieve the holdings we have just set
        verify_holdings = self.transaction_portfolios_api.get_holdings(scope=scope,
                                                                       code=code,
                                                                       effective_at=effective_at,
                                                                       instrument_property_keys=[
                                                                           'Instrument/default/ClientInternal'])

        # Check that the correct number of holdings have been set
        self.assertEqual(verify_holdings.count, len(holding_adjustments),
                         'Got {} holdings when we expected {} holdings'.format(verify_holdings.count,
                                                                               len(holding_adjustments)))

        # Create a dictionary of our adjust holding requests using the instrument uid as the key
        adjustment_requests = {}

        # Here we handle that currencies and instruments use different identifier schemes
        for adjustment in holding_adjustments:
            if 'Instrument/default/ClientInternal' in adjustment.instrument_identifiers.keys():
                key = adjustment.instrument_identifiers['Instrument/default/ClientInternal']
            else:
                key = 'CCY_' + adjustment.instrument_identifiers['Instrument/default/Currency']

            adjustment_requests[key] = adjustment.tax_lots[0]

        # Iterate over our holdings we just retrieved
        for holding in verify_holdings.values:
            # Use the ClientIdentifier if it is an instrument
            if 'LUID' in holding.instrument_uid:
                identifier = holding.properties[0].value
            # Otherwise use the currency code
            else:
                identifier = holding.instrument_uid

            adjustment = adjustment_requests[identifier]

            self.assertEqual(adjustment.units, holding.units,
                             'Holding total units is {} when it should be {}'.format(holding.units,
                                                                                     adjustment.units))

            self.assertEqual(adjustment.cost.amount, holding.cost.amount,
                             'Total amount is {} when it should be {}'.format(holding.cost.amount,
                                                                              adjustment.cost.amount))

            self.assertEqual(adjustment.cost.currency, holding.cost.currency,
                             'Currency is {} when it should be {}'.format(holding.cost.currency,
                                                                          adjustment.cost.currency))

            self.assertEqual(round(adjustment.portfolio_cost, 2), round(holding.cost_portfolio_ccy.amount, 2),
                             'Portfolio cost is {} when it should be {}'.format(
                                 holding.cost_portfolio_ccy.amount,
                                 round(adjustment.portfolio_cost, 2)))

    def reconcile_portfolios_asserts(self,
                                     portfolio_left_scope,
                                     portfolio_left_code,
                                     portfolio_left_effective_date,
                                     portfolio_left_as_at,
                                     portfolio_right_scope,
                                     portfolio_right_code,
                                     portfolio_right_effective_date,
                                     portfolio_right_as_at,
                                     transactions=None,
                                     check_same=True):
        """
        This method contains a set of tests used to test that two portfolios reconcile, we test for one of two things:

        A) If check_same is True we check that both portfolios are identical, in this case we test that:
        - The count of reconciliation breaks on the reconciliation is 0
        - The number of reconciliation breaks returned is 0

        B) If check_same is False we check that given a set of transactions on the left portfolio the right has remained
        unchanged, in this case we test that:
        -

        Note that for this test we are making the following assumptions:
        - The reconciliation method is working perfectly without any errors
        - For the check_same == False method that we only have a single currency
        - We only make a single transaction inside each portfolio for each instrument
        """

        reconcile_holdings_left = models.PortfolioReconciliationRequest(
            portfolio_id=models.ResourceId(scope=portfolio_left_scope,
                                           code=portfolio_left_code),
            effective_at=portfolio_left_effective_date,
            as_at=portfolio_left_as_at)

        reconcile_holdings_right = models.PortfolioReconciliationRequest(
            portfolio_id=models.ResourceId(scope=portfolio_right_scope,
                                           code=portfolio_right_code),
            effective_at=portfolio_right_effective_date,
            as_at=portfolio_right_as_at)

        reconcile_holdings_request = models.PortfoliosReconciliationRequest(left=reconcile_holdings_left,
                                                                            right=reconcile_holdings_right,
                                                                            instrument_property_keys=[
                                                                                'Instrument/default/ClientInternal'
                                                                            ])

        reconciliation = self.reconciliations_api.reconcile_holdings(
            portfolios_reconciliation_request=reconcile_holdings_request)

        if check_same:
            self.assertEqual(reconciliation.count, 0,
                             'We have {} differences between the portfolios'.format(reconciliation.count))

            self.assertEqual(len(reconciliation.values), 0,
                             'We have {} differences between the portfolios'.format(len(reconciliation.values)))
        else:
            # We add one here to account for the difference in cash that results from unsynced trades
            self.assertEqual(reconciliation.count, len(transactions) + 1,
                             'Only {} of {} transactions have been applied'.format(reconciliation.count,
                                                                                   len(transactions)))
            transaction_requests = {}
            for transaction in transactions:

                if 'Instrument/default/ClientInternal' in transaction.instrument_identifiers.keys():
                    key = 'Instrument/default/ClientInternal'
                else:
                    key = 'Instrument/default/Currency'

                transaction_requests[transaction.instrument_identifiers[key]] = transaction

            # Check that for breaks and transactions with the same instrument that the breaks match
            for reconciliation_break in reconciliation.values:
                if 'CCY' not in reconciliation_break.instrument_uid:
                    transaction = transaction_requests[reconciliation_break.instrument_properties[0].value]
                    self.assertEqual(abs(reconciliation_break.difference_units), transaction.units)

    def transactions_added_asserts(self,
                                   portfolio_scope,
                                   portfolio_code,
                                   start_date,
                                   end_date,
                                   as_at_date,
                                   batch_transactions_request):

        """
        This method contains a set of asserts used to test that transactions have been correctly upserted, we test that:
        - The number of transactions added is correct
        - The transaction type is correct
        - The transaction instrument id is correct
        - The transaction units are correct
        - The transaction price is correct
        - The transaction price type i.e. price, yield etc. is correct
        - The transaction total consideration amount is correct
        - The transaction total consideration currency is correct
        - The transaction currency is correct
        - The transaction source i.e. client, internal is correct

        Note that for this test we are making the following assumptions:
        - The Get Transactions method is working correctly
        - There are no transactions outside this request added to the portfolio between the start and end dates 
        """

        transactions = self.transaction_portfolios_api.get_transactions(scope=portfolio_scope,
                                                                        code=portfolio_code,
                                                                        from_transaction_date=start_date,
                                                                        to_transaction_date=end_date,
                                                                        as_at=as_at_date)

        self.assertEqual(transactions.count, len(batch_transactions_request),
                         'Returned {} transactions when expecting {}'.format(transactions.count,
                                                                             len(batch_transactions_request)))

        transaction_requests = {transaction.transaction_id: transaction for transaction in batch_transactions_request}

        for transaction in transactions.values:

            transaction_request = transaction_requests[transaction.transaction_id]

            self.assertEqual(transaction.type, transaction_request.type)

            if 'Instrument/default/ClientInternal' in transaction_request.instrument_identifiers.keys():
                key = 'Instrument/default/ClientInternal'
            else:
                key = 'Instrument/default/Currency'

            self.assertEqual(transaction.instrument_identifiers[key], transaction_request.instrument_identifiers[key])

            # Note that the output date

            self.assertEqual(transaction.transaction_date.isoformat(), transaction_request.transaction_date)
            self.assertEqual(transaction.settlement_date.isoformat(), transaction_request.settlement_date)

            self.assertEqual(transaction.units, transaction_request.units)
            self.assertEqual(transaction.transaction_price.price, transaction_request.transaction_price.price)
            self.assertEqual(transaction.transaction_price.type, transaction_request.transaction_price.type)
            self.assertEqual(transaction.total_consideration.amount,
                             transaction_request.total_consideration.amount)
            self.assertEqual(transaction.total_consideration.currency,
                             transaction_request.total_consideration.currency)
            self.assertEqual(transaction.transaction_currency, transaction_request.transaction_currency)
            self.assertEqual(transaction.source, transaction_request.source)

    def create_property_definition_asserts(self, property_request, property):
        """
        This method contains a set of tests used to test that a property definition has been created successfully, we
        test that:
        - The property definition has been created in the correct domain
        - The property definition has been created in the correct scope
        - The property definition has been created with the correct code
        - The property definition has been created with the correct setting for value required i.e. True or False
        - The property definition has been created with the correct display name
        - The property definition has been created with a data type from the correct scope
        - The property definition has been created with a data type with the correct code
        """

        self.assertEqual(property.domain, property_request.domain)
        self.assertEqual(property.scope, property_request.scope)
        self.assertEqual(property.code, property_request.code)
        self.assertEqual(property.value_required, property_request.value_required)
        self.assertEqual(property.display_name, property_request.display_name)
        self.assertEqual(property.data_type_id.scope, property.data_type_id.scope)
        self.assertEqual(property.data_type_id.code, property.data_type_id.code)

    def reconciliation_asserts(self,
                               reconciliation_break_response,
                               left_scope,
                               left_code,
                               left_effective_at,
                               right_scope,
                               right_code,
                               right_effective_at):
        """
        This function contains a set of assertions which ensure that a reconciliation has been conducted correctly.

        :param reconciliation_break_response: The response from our reconciliation request to LUSID
        :param left_scope: The scope of our left portfolio
        :param left_code: The code of our left portfolio
        :param left_effective_at: The effectiveAt date in ISO8601 format for our left portfolio
        :param right_scope: The scope of our right portfolio
        :param right_code: The code of our right portfolio
        :param right_effective_at: The effectiveAt date in ISO8601 format for our right portfolio
        :return:
        """

        def get_holdings(scope, code, effective_at):
            """
            This function gets a set of holdings from LUSID for a given portfolio. It then takes those holdings
            and puts them into a dictionary containing a list of holdings for each unique instrument. This is
            required as there may be multiple holdings for each instrument. For example for a cash instrument such
            as the Pound Sterling (represented by the instrument identifier 'CCY_GBP') LUSID has a number of different
            holdings types under which it may be held. For cash sitting at the bank this may be represented as a cash
            balance, for cash that is to be paid for a recent transaction this may be represented as committed cash.

            When we do a reconciliation all of these holding types are aggregated. Thus in order for us to check that
            our reconciliation is correct we must also perform this aggregation. By creating a dictionary with a list
            of the holdings for each unique instrument we will be able to do this later.

            :param scope: The scope of the portfolio to get the holdings from
            :param code: The code of the portfolio to get the holdings from
            :param effective_at: The effectiveAt date in ISO8601 format for which we want to get the holdings

            :return:
            holdings: A dictionary containing a list of holdings for each unique instrument
            """
            # Get our holdings from LUSID
            holdings_ = self.transaction_portfolios_api.get_holdings(scope=scope,
                                                                     code=code,
                                                                     effective_at=effective_at)
            # Convert to a dictionary with the instrument uid as the key and a list of holdings as values
            holdings = {}
            for holding in holdings_.values:
                holdings.setdefault(holding.instrument_uid, []).append(holding)
            return holdings

        def aggregate_holdings(holdings):
            """
            This function takes a list of holdings for a given instrument and if there is more than one aggregates the
            number of units and the cost of the holdings.

            :param holdings: A list of holdings for a given instrument

            :return:
            holding_units: The total number of units held in this instrument
            holding_cost_amount: The total cost of units held in this instrument
            holding_cost_currency: The currency of units held in this instrument
            """

            # If we have more than one holding, use our aggregation logic
            if len(holdings) > 1:
                # Extract our units from each of our holdings objects
                holding_units_ = [holding.units for holding in holdings]
                # Extract our cost amount from each of our holdings objects
                holding_cost_amount_ = [holding.cost.amount for holding in holdings]
                # Sum the units and cost amount, rounding to the appropriate level of decimal places
                holding_units = round(reduce((lambda x, y: x + y), holding_units_), 0)
                holding_cost_amount = round(reduce((lambda x, y: x + y), holding_cost_amount_), 2)

            # Otherwise just use the first and only holding
            else:
                holding_units = round(holdings[0].units, 0)
                holding_cost_amount = round(holdings[0].cost.amount, 2)

            # Currency is assumed to be the same across all holdings for each instrument
            holding_cost_currency = holdings[0].cost.currency

            return holding_units, holding_cost_amount, holding_cost_currency

        # Get our left and right holdings
        left_holdings = get_holdings(left_scope, left_code, left_effective_at)
        right_holdings = get_holdings(right_scope, right_code, right_effective_at)

        # Convert our reconciliation breaks to a dictionary with the instrument uid as the key
        rec_breaks = {rec_break.instrument_uid: rec_break for rec_break in reconciliation_break_response.values}

        # Iterate over our left holdings and check that any breaks are correct
        for key, left_holding in left_holdings.items():
            # If there is more than one holding for an instrument, aggregate the holdings
            left_holding_units, left_holding_cost_amount, left_holding_cost_currency = aggregate_holdings(left_holding)
            # Try and find a holding on the right side for the same instruments  
            if key in right_holdings:
                right_holding = right_holdings[key]
                # If there is more than one holding for an instrument, aggregate the holdings
                right_holding_units, right_holding_cost_amount, right_holding_cost_currency = aggregate_holdings(
                    right_holding)
                # Calculate the differences between the two holdings
                difference_units = round(right_holding_units - left_holding_units, 0)
                difference_cost_amount = round(right_holding_cost_amount - left_holding_cost_amount, 2)
                # If there are any differences check that they match our reconciliation break
                if abs(difference_units) > 0 or abs(difference_cost_amount) > 0:
                    rec_break = rec_breaks[key]
                    self.assertEqual(difference_units, round(rec_break.difference_units, 0))
                    self.assertEqual(difference_cost_amount, round(rec_break.difference_cost.amount, 2))
                    self.assertEqual(left_holding_units, round(rec_break.left_units, 0))
                    self.assertEqual(left_holding_cost_amount, round(rec_break.left_cost.amount, 2))
                    self.assertEqual(left_holding_cost_currency, rec_break.left_cost.currency)
                    self.assertEqual(right_holding_units, round(rec_break.right_units, 0))
                    self.assertEqual(right_holding_cost_amount, round(rec_break.right_cost.amount, 2))
                    self.assertEqual(right_holding_cost_currency, rec_break.right_cost.currency)

            # If there is no matching holding on the right, check that the reconciliation break matches the left side
            else:
                rec_break = rec_breaks[key]
                self.assertEqual(left_holding_units, round(rec_break.difference_units, 0))
                self.assertEqual(left_holding_cost_amount, round(rec_break.difference_cost.amount, 2))
                self.assertEqual(left_holding_cost_currency, rec_break.difference_cost.currency)
                self.assertEqual(left_holding_units, round(rec_break.left_units, 0))
                self.assertEqual(left_holding_cost_amount, round(rec_break.left_cost.amount, 2))
                self.assertEqual(left_holding_cost_currency, rec_break.left_cost.currency)

    def add_transaction_property_asserts(self, scope, code, transaction_id, property_key, property_value):
        """
        This method contains a set of assertions which test that a property has been successfully added to a transaction

        :param scope: The scope of the portfolio that contains the transaction
        :param code: The code of the portfolio that contains the transaction
        :param transaction_id: The transaction id of the transaction
        :param property_key: The property key of the property that we want to check
        :param property_value: The property value of the property that we want to check
        """
        # Get our transaction by filtering on the transaction id across all transactions inside our portfolio
        transaction = self.transaction_portfolios_api.get_transactions(scope,
                                                                       code,
                                                                       filter="transactionId eq '{}'".format(
                                                                           transaction_id)).values[0]

        # Create a dictionary with the key, value pairs for each of our properties on the transaction
        transaction_properties = {trans_property.key: trans_property.value for trans_property in transaction.properties}

        # Check that the property exists and that the value is correct
        self.assertTrue(property_key in transaction_properties)
        self.assertEqual(property_value, transaction_properties[property_key])

    def verify_portfolio_group_aggregation_asserts(self,
                                                   aggregated_response,
                                                   portfolio_group_scope,
                                                   portfolio_group_code,
                                                   effective_at):

        """
        This methods contains a set of assertions which test that a portfolio group aggregation was successful. It
        assumes that the metrics you want are the units and cost of the holdings and that we sum across these units.

        :param aggregated_response: The response from the aggregation request
        :param portfolio_group_scope: The scope of the portfolio group
        :param portfolio_group_code: The code of the portfolio group
        :param effective_at: The effecitveAt date of the aggregation request
        """

        # Get the details of our portfolio group including all the portfolios in the group
        portfolio_group = self.portfolio_groups_api.get_portfolio_group(scope=portfolio_group_scope,
                                                                        code=portfolio_group_code)
        # Initialise our aggregate holdings
        agg_holdings = {}
        # Iterate over each portfolio grouping holdings by instrument and currency
        for portfolio in portfolio_group.portfolios:
            # Get the holdings for the current portfolio
            portfolio_holdings = self.transaction_portfolios_api.get_holdings(scope=portfolio.scope,
                                                                              code=portfolio.code,
                                                                              effective_at=effective_at)
            # Iterate over our holdings for the current portfolio
            for holding in portfolio_holdings.values:
                # If the holding is a cash instrument, set the key using the cash format
                if 'CCY' in holding.instrument_uid:
                    key = 'Currency={}'.format(holding.cost.currency)
                # Else, set the key using the instrument format
                else:
                    key = 'LusidInstrumentId={}/{}'.format(holding.instrument_uid, holding.cost.currency)
                # Create the key in our agg holdings dictionary, if it already exists append the holding
                agg_holdings.setdefault(key, []).append((holding.units, holding.cost.amount))

        # Iterate over our holdings grouped by instrument and currency
        for key, holdings in agg_holdings.items():
            # If there is more than one holding, sum all the units and all the cost
            if len(holdings) > 1:
                # Sum our cost and holdings by unzipping our (unit, cost) pairs into (unit, unit....) (cost, cost..)
                agg_holdings[key] = [sum(tup) for tup in list(zip(*holdings))]
                # Change format to a list containing a tuple to match our records with only one holding
                agg_holdings[key] = [(agg_holdings[key][0], agg_holdings[key][1])]

        # Iterate over our aggregated results
        for agg_record in aggregated_response.data:
            # Select our aggregated holding
            agg_holding = agg_holdings[agg_record['Holding/default/SubHoldingKey']]
            # Ensure that the units and cost match
            self.assertEqual(agg_record['Sum(Holding/default/Units)'], agg_holding[0][0])
            self.assertEqual(agg_record['Sum(Holding/default/Cost)'], agg_holding[0][1])


if __name__ == '__main__':
    unittest.main()
