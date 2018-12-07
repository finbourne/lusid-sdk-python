import unittest
import requests
import json
import os
import lusid
import lusid.models as models
from unittest import TestCase
from msrest.authentication import BasicTokenAuthentication
from datetime import datetime, timedelta

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestFinbourneApi(TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        '''
        Here we handle authentication. We use a username, password, client ID and client secret to authenticate
        our account. Once authenticated we retrieve an API token which we can use for future requests using
        '''
        # Load our configuration details
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "secrets.json"), "r") as secrets:
            config = json.load(secrets)
        # Set our authentication details
        token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
        username = os.getenv("FBN_USERNAME", config["api"]["username"])
        password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
        client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
        client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
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
        credentials = BasicTokenAuthentication(TestFinbourneApi.api_token)
        cls.client = lusid.LUSIDAPI(credentials, TestFinbourneApi.api_url)

    def portfolio_creation_tests(self, portfolio, portfolio_request, scope):
        '''
        This method contains a set of tests used to test the successful creation of a portfolio
        '''
        self.assertNotIsInstance(portfolio, models.ErrorResponse,
                                 'No portfolio created, error returned')
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

        # tk - Need to test for base currency, how do I find it? What does it mean? Can it be wrong? Is it validated?

    def portfolio_group_creation_tests(self, portfolio_group, portfolio_group_request, group_scope):
        '''
        This method contains a set of tests used to test the successful creation of a portfolio group
        '''
        self.assertNotIsInstance(portfolio_group, models.ErrorResponse,
                                 'Portfolio group not created, error returned')

        self.assertEqual(portfolio_group.id.code, portfolio_group_request.id,
                         'Portfolio group code is {} instead of {}'.format(portfolio_group.id.code,
                                                                           portfolio_group_request.id))

        self.assertEqual(portfolio_group.description, portfolio_group_request.description,
                         'Portfolio group description is {} instead of {}'.format(portfolio_group.description,
                                                                           portfolio_group_request.description))

        self.assertEqual(portfolio_group.display_name, portfolio_group_request.display_name,
                         'Portfolio group display name is {} instead of {}'.format(portfolio_group.display_name,
                                                                                   portfolio_group_request.display_name))

        # tk - need test for sub_groups

        self.assertEqual(len(portfolio_group.portfolios), len(portfolio_group_request.values),
                         'Portfolio group has {} portfolios instead of {}'.format(portfolio_group.description,
                                                                                  portfolio_group_request.description))

        '''
        Iterate over the portfolios checking that the scope and code is correct. Note that this currently does not
        support the case where none or less than all of the portfolios match. All it handles is if the code matches
        so does the scope. 
        '''
        # Iterate over the portfolios in our group
        for portfolio in portfolio_group.portfolios:
            # Iterate over the portfolios in our request
            for portfolio_request in portfolio_group_request.values:
                if portfolio.code == portfolio_request.code:
                    self.assertEqual(portfolio.scope, portfolio_request.scope,
                                     'Portfolio {} has scope {} instead of {}'.format(portfolio.code,
                                                                                      portfolio.scope,
                                                                                      portfolio_request.scope))



    def derived_portfolio_creation_tests(self, derived_portfolio, derived_portfolio_request):
        '''
        This method contains a set of tests used to test the successful creation of a derived portfolio
        '''

        self.assertEqual(derived_portfolio.is_derived, True,
                         'Expected derived portfolio to be True instead it is {}'.format(derived_portfolio.is_derived))

        self.assertEqual(derived_portfolio_request.code, derived_portfolio.id.code,
                         'Portfolio created with code {} instead of code {}'.format(derived_portfolio.id.code,
                                                                                    derived_portfolio_request.code))

        self.assertEqual(self.test_scope_code, derived_portfolio.id.scope,
                         'Portfolio created in scope {} instead of scope {}'.format(derived_portfolio.id.scope,
                                                                                    self.production_scope_code))

        self.assertEqual(derived_portfolio_request.display_name, derived_portfolio.display_name,
                         'Portfolio created with name {} instead of {}'.format(derived_portfolio.display_name,
                                                                               derived_portfolio_request.display_name))

        self.assertEqual(derived_portfolio_request.description, derived_portfolio.description,
                         'Portfolio created with description {} instead of {}'.format(derived_portfolio.description,
                                                                                      derived_portfolio_request.description))

        self.assertEqual(derived_portfolio_request.parent_portfolio_id,
                         derived_portfolio.parent_portfolio_id,
                         'Portfolio created with description {} instead of {}'.format(
                             derived_portfolio.parent_portfolio_id,
                             derived_portfolio_request.parent_portfolio_id))

    def instrument_upsert_tests(self, batch_upsert_response, batch_upsert_request):
        '''
        This method contains a set of tests used to test the successful upsertion of instruments
        '''
        # Confirm that the response is as expected
        self.assertLess(len(batch_upsert_response.failed), 1,
                        '{} upsert requests of {} failed'.format(len(batch_upsert_response.failed),
                                                                 len(batch_upsert_request)))
        self.assertEqual(len(batch_upsert_response.values), len(batch_upsert_request),
                         'Only {} upsert requests of {} successfully upserted'.format(len(batch_upsert_request),
                                                                                      len(
                                                                                          batch_upsert_response.values)))
        for result in batch_upsert_response.values:
            instrument = batch_upsert_response.values[result]
            self.assertIsNotNone(instrument.lusid_instrument_id,
                                 'Instrument does not have a lusitd instrument id')
            self.assertIn(instrument.name, list(batch_upsert_request.keys()),
                          'The instrument name {} is not in those in the request {}'.format(instrument.name,
                                                                                            batch_upsert_request.keys()))
            self.assertEqual(instrument.identifiers, batch_upsert_request[instrument.name].identifiers,
                             'The instrument has mismatched identifiers to the request')

    def verify_holdings_tests(self, holding_adjustments, holdings, scope, code, effective_at):
        '''
        This method contains a set of tests used to test that set holdings has worked correctly
        '''
        # Check that we got a link back on our response to setting holdings
        self.assertIsNotNone(holdings.href, 'No hyperlink to holdings returned')
        # As we only get links back from our set holdings method, we need to retrieve the holdings we have just
        # set to compare them to the request
        verify_holdings = self.client.get_holdings(scope=scope,
                                                   code=code,
                                                   effective_at=effective_at)

        self.assertEqual(verify_holdings.count, len(holding_adjustments),
                         'Got {} holdings when we expected {} holdings'.format(verify_holdings.count,
                                                                               holding_adjustments))

        for holding in verify_holdings.values:
            for adjustment in holding_adjustments:
                if holding.instrument_uid == adjustment.instrument_uid:

                    self.assertEqual(adjustment.tax_lots[0].units, holding.units,
                                     'Holding total units is {} when it should be {}'.format(holding.units,
                                                                                             adjustment.tax_lots[
                                                                                                 0].units))
                    self.assertEqual(adjustment.tax_lots[0].cost.amount, holding.cost.amount,
                                     'Total amount is {} when it should be {}'.format(holding.cost.amount,
                                                                                      adjustment.tax_lots[
                                                                                          0].cost.amount))
                    self.assertEqual(adjustment.tax_lots[0].cost.currency, holding.cost.currency,
                                     'Currency is {} when it should be {}'.format(holding.cost.currency,
                                                                                  adjustment.tax_lots[0].cost.currency))

                    # self.assertEqual(adjustment.tax_lots[0].portfolio_cost, holding.cost_portfolio_ccy.amount,
                    #                'Portfolio cost is {} when it should be {}'.format(holding.cost_portfolio_ccy.amount,
                    #                                                                  adjustment.tax_lots[0].portfolio_cost))

                    # tk - Where is price?

    def reconcile_portfolios_tests(self,
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

            for reconciliation_break in reconciliation.values:
                for transaction in transactions:
                    if reconciliation_break.instrument_uid == transaction.instrument_uid:

                        # tk - Need better testing here to handle the direction as well as absolute amount
                        self.assertEqual(abs(reconciliation_break.difference_units), transaction.units)
                        # tk - Also need to think about pricing and making sure the holding value is update correctly
            # tk - Need to also check that cash balance is accurate

    def transactions_added_tests(self,
                                 portfolio_scope,
                                 portfolio_code,
                                 start_date,
                                 end_date,
                                 as_at_date,
                                 batch_transactions_request):

        transactions = self.client.get_transactions(scope=portfolio_scope,
                                                    code=portfolio_code,
                                                    from_transaction_date=start_date,
                                                    to_transaction_date=end_date,
                                                    as_at_date=as_at_date)

        self.assertEqual(transactions.count, len(batch_transactions_request),
                         'Returned {} transactions when expecting {}'.format(transactions.count,
                                                                             len(batch_transactions_request)))

        for transaction in transactions.values:
            for transaction_request in batch_transactions_request:
                if transaction.transaction_id == transaction_request.transaction_id:

                    self.assertEqual(transaction.type, transaction_request.type)
                    self.assertEqual(transaction.instrument_uid, transaction_request.instrument_uid)
                    # self.assertEqual(transaction.transaction_date, transaction_request.transaction_date)
                    # self.assertEqual(transaction.settlement_date, transaction_request.settlement_date)
                    self.assertEqual(transaction.units, transaction_request.units)
                    self.assertEqual(transaction.transaction_price.price, transaction_request.transaction_price.price)
                    self.assertEqual(transaction.transaction_price.type, transaction_request.transaction_price.type)
                    self.assertEqual(transaction.total_consideration.amount,
                                     transaction_request.total_consideration.amount)
                    self.assertEqual(transaction.total_consideration.currency,
                                     transaction_request.total_consideration.currency)
                    # tk - exchange_rate
                    self.assertEqual(transaction.transaction_currency, transaction_request.transaction_currency)
                    # tk - properties
                    # tk - counterpartyId
                    self.assertEqual(transaction.source, transaction_request.source)
                    # tk - nettingSet

    # tk - should I check that the holdings have been updated? With the tests above if the transactions didn't update the holdings it would still pass
    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()