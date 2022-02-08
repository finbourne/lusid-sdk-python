import unittest
import uuid
from datetime import datetime

import pytz

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class Portfolios(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()

        cls.test_data_utilities = TestDataUtilities(cls.transaction_portfolios_api)

    @lusid_feature("F1-4")
    def test_create_portfolio(self):
        guid = str(uuid.uuid4())

        # details of the new portfolio to be created, created here with the minimum set of mandatory fields
        request = models.CreateTransactionPortfolioRequest(

            # descriptive name for the portfolio
            display_name="portfolio-{0}".format(guid),

            # unique portfolio code, portfolio codes must be unique across scopes
            code="id-{0}".format(guid),
            base_currency="GBP")

        # create the portfolio in LUSID in the specified scope
        result = self.transaction_portfolios_api.create_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_transaction_portfolio_request=request)

        self.assertEqual(result.id.code, request.code)

    @lusid_feature("F1-1")
    def test_create_portfolio_with_properties(self):
        guid = str(uuid.uuid4())
        property_name = "fund-style-{0}".format(guid)
        data_type_id = models.ResourceId("system", "string")

        #   property definition
        property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=TestDataUtilities.tutorials_scope,
            code=property_name,
            value_required=False,
            display_name="Fund Style",
            life_time="Perpetual",
            data_type_id=data_type_id
        )

        #   create the property definition
        property_definition_result = self.property_definitions_api.create_property_definition(
            create_property_definition_request=property_definition)

        #  property value
        property_value = "Active"
        portfolio_property = models.ModelProperty(key=property_definition_result.key,
                                                  value=models.PropertyValue(label_value=property_value))

        #  details of the portfolio to be created
        request = models.CreateTransactionPortfolioRequest(display_name="portfolio-{0}".format(guid),
                                                           code="id-{0}".format(guid),
                                                           base_currency="GBP",

                                                           # set the property value when creating the portfolio
                                                           properties={
                                                               property_definition_result.key: portfolio_property
                                                           })

        # create the portfolio
        portfolio = self.transaction_portfolios_api.create_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_transaction_portfolio_request=request)

        portfolio_code = portfolio.id.code
        self.assertEqual(portfolio_code, request.code)

        portfolio_properties = self.portfolios_api.get_portfolio_properties(TestDataUtilities.tutorials_scope,
                                                                            portfolio_code)

        self.assertEqual(len(portfolio_properties.properties), 1)
        self.assertEqual(portfolio_properties.properties[property_definition_result.key].value.label_value, property_value)

    @lusid_feature("F13-8")
    def test_add_transaction_to_portfolio(self):
        # effective date of the portfolio, this is the date the portfolio was created and became live.  All dates/times
        # must be supplied in UTC
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # create the portfolio
        portfolio_id = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        #   details of the transaction to be added
        transaction = models.TransactionRequest(

            # unique transaction id
            transaction_id=str(uuid.uuid4()),

            # transaction type, configured during system setup
            type="Buy",
            instrument_identifiers={TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]},
            transaction_date=effective_date,
            settlement_date=effective_date,
            units=100,
            transaction_price=models.TransactionPrice(12.3),
            total_consideration=models.CurrencyAndAmount(1230, "GBP"),
            source="Client"
        )

        #   add the transaction
        self.transaction_portfolios_api.upsert_transactions(
            TestDataUtilities.tutorials_scope,
            portfolio_id,
            transaction_request=[transaction])

        #   get the trades
        trades = self.transaction_portfolios_api.get_transactions(TestDataUtilities.tutorials_scope, portfolio_id)

        self.assertEqual(len(trades.values), 1)
        self.assertEqual(trades.values[0].transaction_id, transaction.transaction_id)

    @lusid_feature("F13-4")
    def test_add_transaction_to_portfolio_with_property(self):
        guid = str(uuid.uuid4())
        property_name = "traderId-{0}".format(guid)

        #   details of the property to be created
        property_definition = models.CreatePropertyDefinitionRequest(

            # The domain the property is to be applied to
            domain="Transaction",

            # the scope the property will be created in
            scope=TestDataUtilities.tutorials_scope,

            life_time="Perpetual",

            # when the property value is set it will be valid forever and cannot be changed.
            # properties whose values can change over time should be created with LifeTimeEnum.TIMEVARIANT
            code=property_name,
            value_required=False,
            display_name="Trader Id",
            data_type_id=models.ResourceId("system", "string")
        )

        #   create the property definition
        property_definition_result = self.property_definitions_api.create_property_definition(
            create_property_definition_request=property_definition)

        # effective date for which portfolio is created
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # create the portfolio
        portfolio_id = self.test_data_utilities.create_transaction_portfolio(TestDataUtilities.tutorials_scope)

        property_value_as_string = "A Trader"
        property_value = models.PropertyValue(property_value_as_string)

        #   details of the transaction to be added
        transaction = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="Buy",
            instrument_identifiers={TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]},
            transaction_date=effective_date,
            settlement_date=effective_date,
            units=100,
            transaction_price=models.TransactionPrice(12.3),
            total_consideration=models.CurrencyAndAmount(1230, "GBP"),
            source="Client",

            # add the property to the transaction
            properties={property_definition_result.key: models.PerpetualProperty(property_definition_result.key, property_value)}
        )

        #   add the transaction
        self.transaction_portfolios_api.upsert_transactions(
            TestDataUtilities.tutorials_scope,
            portfolio_id,
            transaction_request=[transaction])

        #   get the trades
        trades = self.transaction_portfolios_api.get_transactions(TestDataUtilities.tutorials_scope, portfolio_id)

        self.assertEqual(len(trades.values), 1)
        self.assertEqual(trades.values[0].transaction_id, transaction.transaction_id)
        self.assertEqual(trades.values[0].properties[property_definition_result.key].value.label_value, property_value_as_string)

    @lusid_feature("F19-1")
    def test_list_scopes(self):
        # Get the list of scopes across all entities
        scopes = self.scopes_api.list_scopes()

        self.assertGreater(len(scopes.values), 0)

    @lusid_feature("F2-4")
    def test_list_portfolios(self):
        # This defines the scope that the portfolios will be retrieved from
        scope = TestDataUtilities.tutorials_scope + str(uuid.uuid4())

        for i in range(10):
            self.test_data_utilities.create_transaction_portfolio(scope)

        # Retrieve the list of portfolios
        portfolios = self.portfolios_api.list_portfolios_for_scope(scope)

        self.assertEqual(len(portfolios.values), 10)
