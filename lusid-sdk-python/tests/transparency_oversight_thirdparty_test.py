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
        We are an asset manager who has outsourced our fund accounting. We have multiple clients each with multiple
        portfolios containing different investment strategies and priorities.

        Unfortunately we have recently been seeing significant outflows from our fund into passive asset management.
        To halt these flows we are feeling the pressure to drive superior performance and reduce our costs.

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
        Let us create our portfolios
        '''
        pass

    def create_entitlements(self):
        pass
    def set_holdings(self):
        pass
    def add_daily_transactions(self):
        # Make a late trade (don't tell them yet)
        pass
    def update_fund_accountant_record(self):
        # Use BY instead of Buy
        pass
    def reconcile_records(self):
        pass
    def identify_discrepencies(self):
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