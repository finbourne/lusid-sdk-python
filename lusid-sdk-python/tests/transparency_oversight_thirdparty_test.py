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
from collections import namedtuple
from msrest.authentication import BasicTokenAuthentication
from time import sleep
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
        cls.internal_scope_code = 'internal-{}'.format(internal_scope_id)
        cls.fund_accountant_scope_code = 'fund-accountant-{}'.format(fund_accountant_scope_id)

        '''
        We have three clients each with a varying number of portfolios. In LUSID we can use Portfolio Groups to group
        the different portfolios of each of our clients together. Let us create a unique identifier for each client's
        group of portfolios and then we can build our portfolio codes using this id. 
        '''
        # Also create a code for our portfolio, we will re-use the same code in each scope
        client_1_portfolio_group_id = uuid.uuid4()
        client_2_portfolio_group_id = uuid.uuid4()
        client_3_portfolio_group_id = uuid.uuid4()

        cls.client_portfolios = {
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

    def create_entitlements(self):

    def set_holdings(self):

    def add_daily_transactions(self):
        # Make a late trade (don't tell them yet)

    def update_fund_accountant_record(self):
        # Use BY instead of Buy

    def reconcile_records(self):

    def indentify_discrepencies(self):
        # Understand that it was a late trade (where on the timeline do things start to diverge)

    def adjust_portfolio_holdings(self):

    def change_fund_accountants(self):

