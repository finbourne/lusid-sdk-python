import uuid
from unittest import TestCase
import lusid.models as models
from tests.api_client_builder import ApiClientBuilder


class PortfolioTutorial(TestCase):

    client = None

    @classmethod
    def setUpClass(cls):

        cls.client = ApiClientBuilder().build()

    def test_create_portfolio(self):

        guid = str(uuid.uuid4())

        # This defines the scope that the portfolio will be created in
        scope = "sample-scope"

        # Details of the new portfolio to be created, created here with the minimum set of mandatory fields
        request = models.CreateTransactionPortfolioRequest(

            # Unique portfolio code, portfolio codes must be unique across scopes
            code="id-{0}".format(guid),

            # Descriptive name for the portfolio
            display_name="portfolio-{0}".format(guid),

            base_currency="GBP"
        )

        # Create the portfolio in LUSID
        result = self.client.create_portfolio(scope, request)

        # Confirm that the portfolio was successfully created.  Any failures will result in
        # a ApiException being thrown which contain the relevant response code and error message
        self.assertEqual(result.id.code, request.code)
