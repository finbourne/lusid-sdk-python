import unittest
import uuid
import pytz
import lusid
import lusid.models as models
from collections import namedtuple
from datetime import datetime
from time import sleep
from unittest import TestCase
from api_client_builder import ApiClientBuilder

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestFinbourneApi(TestCase):

    instrumentIds = []

    LUSID_INSTRUMENT_IDENTIFIER = "Instrument/default/LusidInstrumentId"

    @classmethod
    def setUpClass(cls):

        # create a configured API client
        api_client = ApiClientBuilder().build("secrets.json")

        # set up the APIs
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
        cls.property_definition_api = lusid.PropertyDefinitionsApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.analytic_stores_api = lusid.AnalyticsStoresApi(api_client)
        cls.aggregation_api = lusid.AggregationApi(api_client)

        instruments = [
            {"Figi": "BBG000C6K6G9", "Name": "VODAFONE GROUP PLC"},
            {"Figi": "BBG000C04D57", "Name": "BARCLAYS PLC"},
            {"Figi": "BBG000FV67Q4", "Name": "NATIONAL GRID PLC"},
            {"Figi": "BBG000BF0KW3", "Name": "SAINSBURY (J) PLC"},
            {"Figi": "BBG000BF4KL1", "Name": "TAYLOR WIMPEY PLC"}
        ]

        figis_to_create = {
            i["Figi"]: models.InstrumentDefinition(
                name=i["Name"],
                identifiers={
                    "Figi": models.InstrumentIdValue(
                        value=i["Figi"])
                }
            ) for i in instruments
        }

        upsert_response = cls.instruments_api.upsert_instruments(
            requests=figis_to_create)

        if len(upsert_response.failed) != 0:
            raise Exception(upsert_response.failed)

        ids = cls.instruments_api.get_instruments(
            identifier_type="Figi",
            identifiers=[i["Figi"] for i in instruments])

        cls.instrumentIds = [i.lusid_instrument_id for i in ids.values.values()]

    def test_create_portfolio(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        request = models.CreateTransactionPortfolioRequest(display_name="portfolio-{0}".format(guid),
                                                           code="id-{0}".format(guid),
                                                           base_currency="GBP")

        # create the portfolio
        result = self.transaction_portfolios_api.create_portfolio(
            scope=scope,
            create_request=request)

        self.assertEqual(result.id.code, request.code)

    def test_create_portfolio_with_properties(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        property_name = "fund-style-{0}".format(guid)
        data_type_id = models.ResourceId("default", "string")

        #   property definition
        property_definition = models.CreatePropertyDefinitionRequest(
            domain="Portfolio",
            scope=scope,
            code=property_name,
            value_required=False,
            display_name="Fund Style",
            life_time="Perpetual",
            data_type_id=data_type_id
        )

        #   create the property definition
        property_definition_result = self.property_definition_api.create_property_definition(
            definition=property_definition)

        #   create the portfolio
        request = models.CreateTransactionPortfolioRequest(display_name="portfolio-{0}".format(guid),
                                                           code="id-{0}".format(guid),
                                                           base_currency="GBP")

        portfolio = self.transaction_portfolios_api.create_portfolio(
            scope=scope,
            create_request=request)

        self.assertEqual(portfolio.id.code, request.code)

        portfolio_id = portfolio.id.code

        self.assertIsNotNone(portfolio_id)

        #  property value
        property_value = "Active"
        portfolio_property = models.PropertyValue(property_value)

        #   add the property to the portfolio
        properties_result = self.portfolios_api.upsert_portfolio_properties(
            scope, portfolio_id,
            effective_at=portfolio.created,
            portfolio_properties={property_definition_result.key: portfolio_property})

        self.assertEqual(properties_result.origin_portfolio_id.code, portfolio_id)
        self.assertEqual(properties_result.properties[0].value, property_value)

    def test_create_trade_with_property(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        property_name = "traderId-{0}".format(guid)

        #   property definition
        property_definition = models.CreatePropertyDefinitionRequest(
            domain="Trade",
            scope=scope,
            code=property_name,
            value_required=False,
            display_name="Trader Id",
            life_time="Perpetual",
            data_type_id=models.ResourceId("default", "string")
        )

        #   create the property definition
        property_definition_result = self.property_definition_api.create_property_definition(
            definition=property_definition)

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        #   create the portfolio
        request = models.CreateTransactionPortfolioRequest(
            display_name="portfolio-{0}".format(guid),
            code="id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        portfolio = self.transaction_portfolios_api.create_portfolio(
            scope=scope,
            create_request=request)

        self.assertEqual(portfolio.id.code, request.code)

        portfolio_id = portfolio.id.code

        self.assertIsNotNone(portfolio_id)

        property_value = "A Trader"

        #   create the trade
        trade = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="Buy",
            instrument_identifiers={self.LUSID_INSTRUMENT_IDENTIFIER: self.instrumentIds[0]},
            transaction_date=effective_date,
            settlement_date=effective_date,
            units=100,
            transaction_price=models.TransactionPrice(12.3),
            total_consideration=models.CurrencyAndAmount(1230, "GBP"),
            source="Client",
            properties={property_definition_result.key: models.PerpetualPropertyValue(property_value)}
        )

        #   add the trade
        self.transaction_portfolios_api.upsert_transactions(
            scope,
            portfolio_id,
            transactions=[trade])

        #   get the trades
        trades = self.transaction_portfolios_api.get_transactions(scope, portfolio_id)

        self.assertEqual(len(trades.values), 1)
        self.assertEqual(trades.values[0].transaction_id, trade.transaction_id)
        self.assertEqual(trades.values[0].properties[0].value, property_value)

    def test_apply_bitemporal_portfolio_changes(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        request = models.CreateTransactionPortfolioRequest(
            display_name="portfolio-{0}".format(guid),
            code="id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        # create the portfolio
        result = self.transaction_portfolios_api.create_portfolio(
            scope=scope,
            create_request=request)

        self.assertEqual(result.id.code, request.code)

        portfolio_id = result.id.code

        TransactionSpec = namedtuple('TradeSpec', 'id price trade_date')
        trade_specs = [
            TransactionSpec(self.instrumentIds[0], 101, datetime(2018, 1, 1, tzinfo=pytz.utc)),
            TransactionSpec(self.instrumentIds[1], 102, datetime(2018, 1, 2, tzinfo=pytz.utc)),
            TransactionSpec(self.instrumentIds[2], 103, datetime(2018, 1, 3, tzinfo=pytz.utc))
        ]
        trade_specs.sort(key=lambda ts: ts.id)

        new_trades = list(map(self.build_transaction, trade_specs))

        # add initial batch of trades
        initial_result = self.transaction_portfolios_api.upsert_transactions(
            scope,
            portfolio_id,
            transactions=new_trades)
        as_at_batch1 = initial_result.version.as_at_date
        sleep(0.5)

        # add trade for 2018-1-8
        trade = self.build_transaction(
            TransactionSpec(self.instrumentIds[3], 104, datetime(2018, 1, 8, tzinfo=pytz.utc)))
        later_trade = self.transaction_portfolios_api.upsert_transactions(
            scope,
            portfolio_id,
            transactions=[trade])
        as_at_batch2 = later_trade.version.as_at_date
        sleep(0.5)

        # add back dated trade
        trade = self.build_transaction(
            TransactionSpec(self.instrumentIds[4], 105, datetime(2018, 1, 5, tzinfo=pytz.utc)))
        backdated_trade = self.transaction_portfolios_api.upsert_transactions(
            scope,
            portfolio_id,
            transactions=[trade])
        as_at_batch3 = backdated_trade.version.as_at_date
        sleep(0.5)

        def print_transactions(transactions):
            for transaction in transactions:
                print("{0}\t{1}\t{2}\t{3}\t{4}".format(transaction.instrument_uid,
                                                       transaction.transaction_date,
                                                       transaction.units,
                                                       transaction.transaction_price,
                                                       transaction.total_consideration))

        # get the list of original trades
        trades_list = self.transaction_portfolios_api.get_transactions(scope, portfolio_id, as_at=as_at_batch1)

        self.assertEqual(len(trades_list.values), 3, "Initial trades, as at {0}".format(as_at_batch1))
        print("trades at {0}".format(as_at_batch1))
        print_transactions(trades_list.values)

        # get the list of trades including the later trade
        trades_list = self.transaction_portfolios_api.get_transactions(scope, portfolio_id, as_at=as_at_batch2)
        self.assertEqual(len(trades_list.values), 4, "Including later trade, as at {0}".format(as_at_batch2))
        print("trades at {0}".format(as_at_batch2))
        print_transactions(trades_list.values)

        # get the list of trades including the back-dated trade
        trades_list = self.transaction_portfolios_api.get_transactions(scope, portfolio_id, as_at=as_at_batch3)
        self.assertEqual(len(trades_list.values), 5, "Including back-dated trade, as at {0}".format(as_at_batch3))
        print("trades at {0}".format(as_at_batch3))
        print_transactions(trades_list.values)

        # get the list of trades now
        all_trades = self.transaction_portfolios_api.get_transactions(scope, portfolio_id)
        print("trades at {0}".format(datetime.utcnow()))
        print_transactions(all_trades.values)

    def test_add_instruments(self):

        sec_id = "added-sec-{}".format(str(uuid.uuid4()))

        request = models.InstrumentDefinition(
            name="MyInstrument",
            identifiers={
                "ClientInternal": models.InstrumentIdValue(value="MyIdValue")
            }
        )

        self.instruments_api.upsert_instruments(
            requests={sec_id: request})

    def test_portfolio_aggregation(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        request = models.CreateTransactionPortfolioRequest(
            display_name="portfolio-{0}".format(guid),
            code="id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        #   create the portfolio
        result = self.transaction_portfolios_api.create_portfolio(
            scope=scope,
            create_request=request)

        self.assertEqual(result.id.code, request.code)

        portfolio_id = result.id.code

        TransactionSpec = namedtuple('TransactionSpec', 'id price trade_date')
        transaction_specs = [
            TransactionSpec(self.instrumentIds[0], 101, effective_date),
            TransactionSpec(self.instrumentIds[1], 102, effective_date),
            TransactionSpec(self.instrumentIds[2], 103, effective_date)
        ]
        transaction_specs.sort(key=lambda ts: ts.id)

        new_trades = list(map(self.build_transaction, transaction_specs))

        #   add initial batch of trades
        self.transaction_portfolios_api.upsert_transactions(
            scope,
            portfolio_id,
            transactions=new_trades)

        try:
            self.analytic_stores_api.get_analytic_store(
                scope,
                effective_date.year,
                effective_date.month,
                effective_date.day
            )
        except:
            #   create an analytic store
            analytic_store_request = models.CreateAnalyticStoreRequest(scope, effective_date)
            self.analytic_stores_api.create_analytic_store(
                request=analytic_store_request)

        prices = [
            models.InstrumentAnalytic(self.instrumentIds[0], 100),
            models.InstrumentAnalytic(self.instrumentIds[1], 200),
            models.InstrumentAnalytic(self.instrumentIds[2], 300)
        ]

        #   add prices
        self.analytic_stores_api.set_analytics(scope, effective_date.year, effective_date.month, effective_date.day, data=prices)

        aggregation_request = models.AggregationRequest(
            recipe_id=models.ResourceId(scope, "default"),
            metrics=[
                models.AggregateSpec("Instrument/default/Name", "Value"),
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum")
            ],
            group_by=["Instrument/default/Name"],
            effective_at=effective_date
        )

        #   do the aggregation
        aggregation = self.aggregation_api.get_aggregation_by_portfolio(scope, portfolio_id, request=aggregation_request)

        for item in aggregation.data:
            print("\t{}\t{}\t{}".format(item["Instrument/default/Name"], item["Proportion(Holding/default/PV)"],
                                        item["Sum(Holding/default/PV)"]))

    # utility to build trade from spec
    @classmethod
    def build_transaction(cls, trade_spec):
        return models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="StockIn",
            instrument_identifiers={cls.LUSID_INSTRUMENT_IDENTIFIER: trade_spec.id},
            transaction_date=trade_spec.trade_date,
            settlement_date=trade_spec.trade_date,
            units=100,
            transaction_price=models.TransactionPrice(trade_spec.price),
            total_consideration=models.CurrencyAndAmount(100 * trade_spec.price, "GBP"),
            source="Client")


if __name__ == '__main__':
    unittest.main()