import unittest
import uuid

import lusid
import lusid.models as models

from lusidfeature import lusid_feature
from utilities import TestDataUtilities


class ReferencePortfolio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        # Create API client
        api_client = TestDataUtilities.api_client()

        # Instantiate reference portfolio and portfolios API
        cls.reference_portfolio_api = lusid.ReferencePortfolioApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

    @lusid_feature("F39")
    def test_create_reference_portfolio(self):
        guid = str(uuid.uuid4())

        # Details of the new reference portfolio to be created
        request = models.CreateReferencePortfolioRequest(
            display_name=f"portfolio-{guid}",
            description="Test reference portfolio",
            code=f"id-{guid}",
        )

        # Create the reference portfolio in LUSID in the tutorials scope
        result = self.reference_portfolio_api.create_reference_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_reference_portfolio_request=request,
        )

        self.assertEqual(result.id.code, request.code)

        # Delete the portfolio once test complete
        self.portfolios_api.delete_portfolio(
            scope=TestDataUtilities.tutorials_scope, code=result.id.code
        )
