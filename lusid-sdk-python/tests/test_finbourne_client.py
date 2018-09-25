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

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestFinbourneApi(TestCase):
    client = None
    instrumentIds = []

    @classmethod
    def setUpClass(cls):

        #   load configuration
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "secrets.json"), "r") as secrets:
            config = json.load(secrets)

        token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
        username = os.getenv("FBN_USERNAME", config["api"]["username"])
        password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
        client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
        client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
        cls.api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])

        token_request_body = ("grant_type=password&username={0}".format(username) +
                              "&password={0}&scope=openid client groups".format(password) +
                              "&client_id={0}&client_secret={1}".format(client_id, client_secret))

        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
        okta_response = requests.post(token_url, data=token_request_body, headers=headers)

        assert okta_response.status_code == 200

        #   set the okta api token
        cls.api_token = {"access_token": okta_response.json()["access_token"]}

        credentials = BasicTokenAuthentication(TestFinbourneApi.api_token)
        cls.client = lusid.LUSIDAPI(credentials, TestFinbourneApi.api_url)

        figis = ["BBG000C6K6G9", "BBG000C04D57", "BBG000FV67Q4", "BBG000BF0KW3", "BBG000BF4KL1"]
        ids = cls.client.lookup_instruments_from_codes("Figi", figis)

        for v in ids.values.values():
            for s in v:
                cls.instrumentIds.append(s.uid)

    def test_create_portfolio(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        request = models.CreateTransactionPortfolioRequest(display_name="portfolio-{0}".format(guid),
                                                           code="id-{0}".format(guid),
                                                           base_currency="GBP")

        # create the portfolio
        result = self.client.create_portfolio(scope, request)

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
        property_definition_result = self.client.create_property_definition(property_definition)

        #   create the portfolio
        request = models.CreateTransactionPortfolioRequest(display_name="portfolio-{0}".format(guid),
                                                           code="id-{0}".format(guid),
                                                           base_currency="GBP")

        portfolio = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio.id.code, request.code)

        portfolio_id = portfolio.id.code

        self.assertIsNotNone(portfolio_id)

        #  property value
        property_value = "Active"
        portfolio_property = models.CreatePropertyRequest(property_value)

        #   add the property to the portfolio
        properties_result = self.client.upsert_portfolio_properties(scope, portfolio_id,
                                                                    {property_definition_result.key: portfolio_property},
                                                                    portfolio.created)

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
        property_definition_result = self.client.create_property_definition(property_definition)

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        #   create the portfolio
        request = models.CreateTransactionPortfolioRequest(
            "portfolio-{0}".format(guid),
            "id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        portfolio = self.client.create_portfolio(scope, request)

        self.assertEqual(portfolio.id.code, request.code)

        portfolio_id = portfolio.id.code

        self.assertIsNotNone(portfolio_id)

        property_value = "A Trader"

        #   create the trade
        trade = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="Buy",
            instrument_uid=self.instrumentIds[0],
            settlement_currency="GBP",
            transaction_date=effective_date,
            settlement_date=effective_date,
            units=100,
            transaction_price=12.3,
            total_consideration=1230,
            source="Client",
            properties={property_definition_result.key: models.CreatePerpetualPropertyRequest(property_value)}
        )

        #   add the trade
        self.client.upsert_transactions(scope, portfolio_id, [trade])

        #   get the trades
        trades = self.client.get_transactions(scope, portfolio_id)

        self.assertEqual(len(trades.values), 1)
        self.assertEqual(trades.values[0].transaction_id, trade.transaction_id)
        self.assertEqual(trades.values[0].properties[0].value, property_value)

    def test_apply_bitemporal_portfolio_changes(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        request = models.CreateTransactionPortfolioRequest(
            "portfolio-{0}".format(guid),
            "id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        # create the portfolio
        result = self.client.create_portfolio(scope, request)

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
        initial_result = self.client.upsert_transactions(scope, portfolio_id, new_trades)
        as_at_batch1 = initial_result.version.as_at_date
        sleep(0.5)

        # add trade for 2018-1-8
        trade = self.build_transaction(TransactionSpec(self.instrumentIds[3], 104, datetime(2018, 1, 8, tzinfo=pytz.utc)))
        later_trade = self.client.upsert_transactions(scope, portfolio_id, [trade])
        as_at_batch2 = later_trade.version.as_at_date
        sleep(0.5)

        # add back dated trade
        trade = self.build_transaction(TransactionSpec(self.instrumentIds[4], 105, datetime(2018, 1, 5, tzinfo=pytz.utc)))
        backdated_trade = self.client.upsert_transactions(scope, portfolio_id, [trade])
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
        trades_list = self.client.get_transactions(scope, portfolio_id, as_at=as_at_batch1)

        self.assertEqual(len(trades_list.values), 3, "Initial trades, as at {0}".format(as_at_batch1))
        print("trades at {0}".format(as_at_batch1))
        print_transactions(trades_list.values)

        # get the list of trades including the later trade
        trades_list = self.client.get_transactions(scope, portfolio_id, as_at=as_at_batch2)
        self.assertEqual(len(trades_list.values), 4, "Including later trade, as at {0}".format(as_at_batch2))
        print("trades at {0}".format(as_at_batch2))
        print_transactions(trades_list.values)

        # get the list of trades including the back-dated trade
        trades_list = self.client.get_transactions(scope, portfolio_id, as_at=as_at_batch3)
        self.assertEqual(len(trades_list.values), 5, "Including back-dated trade, as at {0}".format(as_at_batch3))
        print("trades at {0}".format(as_at_batch3))
        print_transactions(trades_list.values)

        # get the list of trades now
        all_trades = self.client.get_transactions(scope, portfolio_id)
        print("trades at {0}".format(datetime.utcnow()))
        print_transactions(all_trades.values)

    def test_lookup_instruments(self):

        isins = ["IT0004966401", "FR0010192997"]

        #   lookup instruments
        fbn_ids = self.client.lookup_instruments_from_codes("Isin", isins)

        self.assertGreater(len(fbn_ids.values), 0)

    def test_add_securities(self):

        secid = "added-sec-{}".format(str(uuid.uuid4()))
        self.client.batch_add_client_instruments([models.CreateClientInstrumentRequest(secid, secid, [])])

    def test_portfolio_aggregation(self):

        scope = str(uuid.uuid4())
        guid = str(uuid.uuid4())
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        request = models.CreateTransactionPortfolioRequest(
            "portfolio-{0}".format(guid),
            "id-{0}".format(guid),
            base_currency="GBP",
            created=effective_date
        )

        #   create the portfolio
        result = self.client.create_portfolio(scope, request)

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
        self.client.upsert_transactions(scope, portfolio_id, new_trades)

        try:
            self.client.get_analytic_store(
                scope,
                effective_date.year,
                effective_date.month,
                effective_date.day
            )
        except:
            #   create an analytic store
            analytic_store_request = models.CreateAnalyticStoreRequest(scope, effective_date)
            self.client.create_analytic_store(analytic_store_request)

        prices = [
            models.InstrumentAnalyticDataDto(self.instrumentIds[0], 100),
            models.InstrumentAnalyticDataDto(self.instrumentIds[1], 200),
            models.InstrumentAnalyticDataDto(self.instrumentIds[2], 300)
        ]

        #   add prices
        prices_result = self.client.insert_analytics(scope, effective_date.year, effective_date.month, effective_date.day,
                                                prices)

        aggregation_request = models.AggregationRequest(
            recipe_id=models.ResourceId(scope, "default"),
            metrics=[
                models.AggregateSpec("Holding/default/PV", "Proportion"),
                models.AggregateSpec("Holding/default/PV", "Sum")
            ],
            group_by=["Security/default/CommonName"],
            effective_at=effective_date
        )

        #   do the aggregation
        aggregation = self.client.get_aggregation_by_portfolio(scope, portfolio_id, aggregation_request)

        for item in aggregation.data:
            print("\t{}\t{}\t{}".format(item["Security/default/CommonName"], item["Holding/default/PV%"], item["Holding/default/PV"]))

    # utility to build trade from spec
    @staticmethod
    def build_transaction(trade_spec):
        return models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="StockIn",
            instrument_uid=trade_spec.id,
            settlement_currency="GBP",
            transaction_date=trade_spec.trade_date,
            settlement_date=trade_spec.trade_date,
            units=100,
            transaction_price=trade_spec.price,
            total_consideration=100 * trade_spec.price,
            source="Client")


if __name__ == '__main__':
    unittest.main()
