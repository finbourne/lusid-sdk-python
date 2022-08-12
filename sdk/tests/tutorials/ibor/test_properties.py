import unittest
from datetime import datetime

import pytz
import uuid

import lusid
import lusid.models as models
from lusidfeature import lusid_feature

from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.instrument_loader import InstrumentLoader
from utilities.test_data_utilities import TestDataUtilities
from utilities.credentials_source import CredentialsSource


class Properties(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    def get_guid(self):
        # creates random alphanumeric code
        return str(uuid.uuid4())[:12]

    @lusid_feature("F1-5")
    def test_create_portfolio_with_label_property(self):
        # Details of property to be created
        uuid = self.get_guid()
        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)

        label_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=TestDataUtilities.tutorials_scope,
            code="fund-style-{}".format(uuid),
            display_name="fund style",
            life_time="Perpetual",
            value_required=False,
            data_type_id=models.resource_id.ResourceId(scope="system", code="string")

        )

        # create property definition
        label_property_definition_request = self.property_definitions_api.create_property_definition(
            label_property_definition)

        # create property values
        property_value = models.PropertyValue(label_value="Active")

        # Details of new portfolio to be created
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code="ud-{}".format(uuid),
            display_name="portfolio-{}".format(uuid),
            base_currency="GBP",
            created=effective_date,
            properties={
                label_property_definition_request.key: models.PerpetualProperty(
                    key=label_property_definition_request.key,
                    value=property_value
                )
            }
        )

        # create portfolio
        portfolio_request = self.transaction_portfolios_api.create_portfolio(scope=TestDataUtilities.tutorials_scope,
                                                                             create_transaction_portfolio_request=create_portfolio_request)

        # get properties for assertions
        portfolio_properties = self.portfolios_api.get_portfolio_properties(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_request.id.code).properties

        label_property = portfolio_properties[label_property_definition_request.key]

        # Perform assertions on keys, codes and values
        self.assertEqual(list(portfolio_properties.keys())[0], label_property_definition_request.key)
        self.assertEqual(portfolio_request.id.code, create_portfolio_request.code)
        self.assertEqual(label_property.value.label_value, property_value.label_value)

    @lusid_feature("F1-6")
    def test_create_portfolio_with_metric_property(self):
        uuid = self.get_guid()
        effective_date = datetime(year=2018, month=1, day=1, tzinfo=pytz.utc)

        # details of property to be created
        metric_property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=TestDataUtilities.tutorials_scope,
            code="fund-NAV-{}".format(uuid),
            display_name="fund NAV",
            life_time="Perpetual",
            value_required=False,
            data_type_id=models.resource_id.ResourceId(scope="system", code="number")
        )

        # create property definitions
        metric_property_definition_result = self.property_definitions_api.create_property_definition(metric_property_definition)

        # create the property values
        metric_property_value_request = models.PropertyValue(metric_value=models.MetricValue(value=289884350.173235074209))
        # metric_property_value_request = models.PropertyValue(label_value="Active")

        # Details of the new portfolio to be created, created here with the minimum set of mandatory fields
        create_portfolio_request = models.CreateTransactionPortfolioRequest(
            code="ud-{}".format(uuid),
            display_name="portfolio-{}".format(uuid),
            base_currency="GBP",
            created=effective_date,
            properties={
                metric_property_definition_result.key: models.PerpetualProperty(
                    key=metric_property_definition_result.key,
                    value=metric_property_value_request
                )
            }
        )

        # Create portfolio
        portfolio_result = self.transaction_portfolios_api.create_portfolio(scope=TestDataUtilities.tutorials_scope,
                                                                            create_transaction_portfolio_request=create_portfolio_request)
        portfolio_properties = self.portfolios_api.get_portfolio_properties(scope=TestDataUtilities.tutorials_scope,
                                                                            code=portfolio_result.id.code).properties
        metric_property = portfolio_properties[metric_property_definition_result.key]

        # Perform assertions on codes, keys, values and units
        self.assertEqual(portfolio_result.id.code, create_portfolio_request.code)
        self.assertEqual(list(portfolio_properties.keys())[0], metric_property_definition_result.key)

        print(metric_property.value.metric_value.value)
        self.assertEqual(metric_property.value.metric_value.value, 289884350.17323506)
        self.assertEqual(metric_property.value.metric_value.value, 289884350.173235074)
        self.assertEqual(metric_property.value.metric_value.unit, metric_property_value_request.metric_value.unit)

