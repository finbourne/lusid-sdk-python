import unittest
import requests
import json
import os
import lusid
import lusid.models as models
from unittest import TestCase
from msrest.authentication import BasicTokenAuthentication
from timeit import default_timer as timer

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
        print (func.__name__, ' took ', end-start, ' seconds to execute')
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

        # Load our configuration details from a secrets file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "secrets.json"), "r") as secrets:
            config = json.load(secrets)

        # Get our URL for authentication
        token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])

        # Get our credentials
        username = os.getenv("FBN_USERNAME", config["api"]["username"])
        password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
        client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
        client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))

        # Get our URL for the API
        cls.api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])

        # Prepare our authentication request
        token_request_body = ("grant_type=password&username={0}".format(username) +
                              "&password={0}&scope=openid client groups".format(password) +
                              "&client_id={0}&client_secret={1}".format(client_id, client_secret))
        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # Make our authentication request
        okta_response = requests.post(token_url, data=token_request_body, headers=headers)

        # Ensure that we have a 200 response code
        assert okta_response.status_code == 200

        # Retrieve our api token from the authentication response
        cls.api_token = {"access_token": okta_response.json()["access_token"]}

        # Initialise our API client using our token so that we can include it in all future requests
        credentials = BasicTokenAuthentication(cls.api_token)
        cls.client = lusid.LUSIDAPI(credentials, cls.api_url)

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

        portfolio_requests = {request.code:request for request in portfolio_group_request.values}

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
        verify_holdings = self.client.get_holdings(scope=scope,
                                                   code=code,
                                                   effective_at=effective_at)

        # Check that the correct number of holdings have been set
        self.assertEqual(verify_holdings.count, len(holding_adjustments),
                         'Got {} holdings when we expected {} holdings'.format(verify_holdings.count,
                                                                               len(holding_adjustments)))

        # Create a dictionary of our adjust holding requests using the instrument uid as the key
        adjustment_requests = {adjustment.instrument_uid:adjustment.tax_lots[0] for adjustment in holding_adjustments}

        # Iterate over our holdings we just retrieved
        for holding in verify_holdings.values:
            # Select the matching adjustment request using the instrument uid as the lookup
            adjustment = adjustment_requests[holding.instrument_uid]

            self.assertEqual(adjustment.units, holding.units,
                             'Holding total units is {} when it should be {}'.format(holding.units,
                                                                                     adjustment.units))

            self.assertEqual(adjustment.cost.amount, holding.cost.amount,
                             'Total amount is {} when it should be {}'.format(holding.cost.amount,
                                                                              adjustment.cost.amount))

            self.assertEqual(adjustment.cost.currency, holding.cost.currency,
                             'Currency is {} when it should be {}'.format(holding.cost.currency,
                                                                          adjustment.cost.currency))
            '''
            self.assertEqual(round(adjustment.portfolio_cost, 2), holding.cost_portfolio_ccy.amount,
                             'Portfolio cost is {} when it should be {}'.format(
                                 holding.cost_portfolio_ccy.amount,
                                 round(adjustment.portfolio_cost, 2)))
            '''


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
                                                                            instrument_property_keys=[])

        reconciliation = self.client.reconcile_holdings(request=reconcile_holdings_request)

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

            transaction_requests = {transaction.instrument_uid:transaction for transaction in transactions}

            # Check that for breaks and transactions with the same instrument that the breaks match
            for reconciliation_break in reconciliation.values:
                if 'CCY' not in reconciliation_break.instrument_uid:
                    transaction = transaction_requests[reconciliation_break.instrument_uid]
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

        transactions = self.client.get_transactions(scope=portfolio_scope,
                                                    code=portfolio_code,
                                                    from_transaction_date=start_date,
                                                    to_transaction_date=end_date,
                                                    as_at_date=as_at_date)

        self.assertEqual(transactions.count, len(batch_transactions_request),
                         'Returned {} transactions when expecting {}'.format(transactions.count,
                                                                             len(batch_transactions_request)))

        transaction_requests = {transaction.transaction_id: transaction for transaction in batch_transactions_request}

        for transaction in transactions.values:

            transaction_request = transaction_requests[transaction.transaction_id]

            self.assertEqual(transaction.type, transaction_request.type)
            self.assertEqual(transaction.instrument_uid, transaction_request.instrument_uid)

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

    def create_property_definition_test(self, property_request, property):
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

    def test(self):
        """
        This method is required to set up the class.
        """
        pass

if __name__ == '__main__':
    unittest.main()