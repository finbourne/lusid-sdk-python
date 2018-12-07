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
        client_1_portfolio_group_id = uuid.uuid4()
        client_2_portfolio_group_id = uuid.uuid4()
        client_3_portfolio_group_id = uuid.uuid4()

        self.client_portfolios = {
            'client-{}-portfolios'.format(client_1_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(client_1_portfolio_group_id),
                'client-{}-strategy-tech'.format(client_1_portfolio_group_id),
                'client-{}-strategy-growth'.format(client_1_portfolio_group_id)
            ],
            'client-{}-portfolios'.format(client_2_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(client_2_portfolio_group_id),
                'client-{}-strategy-energy'.format(client_2_portfolio_group_id),
                'client-{}-strategy-fixedincome'.format(client_2_portfolio_group_id),
                'client-{}-strategy-international'.format(client_2_portfolio_group_id),
                'client-{}-strategy-usgovt'.format(client_2_portfolio_group_id)
            ],
            'client-{}-portfolios'.format(client_3_portfolio_group_id): [
                'client-{}-strategy-balanced'.format(client_3_portfolio_group_id),
                'client-{}-strategy-fixedincome'.format(client_3_portfolio_group_id)
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

    def set_holdings(self):
        '''
        Now that we have our portfolios and groups set up for our clients we can add in their current holdings. We will
        being by having the internal scope and the fund account scope to be completely in sync with exactly the same
        holdings. This will be our initial state.
        '''

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

    def test(self):
        self.import_data()
        self.create_portfolios()
        self.create_entitlements()
        self.set_holdings()
        self.add_daily_transactions()
        self.update_fund_accountant_record()
        self.reconcile_records()
        self.identify_discrepencies()
        self.adjust_portfolio_holdings()
        self.change_fund_accountants()

if __name__ == '__main__':
    unittest.main()