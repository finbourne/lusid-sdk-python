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

    LUSID_INSTRUMENT_IDENTIFIER = "Instrument/default/LusidInstrumentId"

    @classmethod
    def setUpClass(cls):

        # Load our configuration details from the environment variables
        token_url = os.getenv("FBN_TOKEN_URL", None)
        cls.api_url = os.getenv("FBN_LUSID_API_URL", None)
        username = os.getenv("FBN_USERNAME", None)
        password_raw = os.getenv("FBN_PASSWORD", None)
        client_id_raw = os.getenv("FBN_CLIENT_ID", None)
        client_secret_raw = os.getenv("FBN_CLIENT_SECRET", None)

        # If any of the environmental variables are missing use a local secrets file
        if token_url is None or username is None or password_raw is None or client_id_raw is None \
                or client_secret_raw is None or cls.api_url is None:

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(dir_path, "secrets.json"), "r") as secrets:
                config = json.load(secrets)

            token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
            username = os.getenv("FBN_USERNAME", config["api"]["username"])
            password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
            client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
            client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
            cls.api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])

        else:
            password = pathname2url(password_raw)
            client_id = pathname2url(client_id_raw)
            client_secret = pathname2url(client_secret_raw)

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
        credentials = BasicTokenAuthentication(cls.api_token)
        cls.client = lusid.LUSIDAPI(credentials, cls.api_url)

        instruments = [
            {"Figi": "BBG000C6K6G9", "Name": "VODAFONE GROUP PLC"},
            {"Figi": "BBG000C04D57", "Name": "BARCLAYS PLC"},
            {"Figi": "BBG000FV67Q4", "Name": "NATIONAL GRID PLC"},
            {"Figi": "BBG000BF0KW3", "Name": "SAINSBURY (J) PLC"},
            {"Figi": "BBG000BF4KL1", "Name": "TAYLOR WIMPEY PLC"}
        ]

        figis_to_create = {i["Figi"]: models.InstrumentDefinition(i["Name"], {"Figi": i["Figi"]}) for i in instruments}

        upsert_response = cls.client.upsert_instruments(figis_to_create)

        if len(upsert_response.failed) != 0:
            raise Exception(upsert_response.failed)

        ids = cls.client.get_instruments("Figi", [i["Figi"] for i in instruments])

        cls.instrumentIds = [i.lusid_instrument_id for i in ids.values.values()]

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
        portfolio_property = models.PropertyValue(property_value)

        #   add the property to the portfolio
        properties_result = self.client.upsert_portfolio_properties(scope, portfolio_id,
                                                                    {
                                                                        property_definition_result.key: portfolio_property},
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
        trade = self.build_transaction(
            TransactionSpec(self.instrumentIds[3], 104, datetime(2018, 1, 8, tzinfo=pytz.utc)))
        later_trade = self.client.upsert_transactions(scope, portfolio_id, [trade])
        as_at_batch2 = later_trade.version.as_at_date
        sleep(0.5)

        # add back dated trade
        trade = self.build_transaction(
            TransactionSpec(self.instrumentIds[4], 105, datetime(2018, 1, 5, tzinfo=pytz.utc)))
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

    @unittest.skip("ISIN not yet supported")
    def test_lookup_instruments(self):

        isins = ["IT0004966401", "FR0010192997"]

        #   lookup instruments
        fbn_ids = self.client.lookup_instruments_from_codes("Isin", isins)

        self.assertGreater(len(fbn_ids.values), 0)

    def test_add_instruments(self):

        sec_id = "added-sec-{}".format(str(uuid.uuid4()))

        request = models.InstrumentDefinition("MyInstrument", {"ClientInternal": "MyIdValue"})

        self.client.upsert_instruments({sec_id: request})

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
            models.InstrumentAnalytic(self.instrumentIds[0], 100),
            models.InstrumentAnalytic(self.instrumentIds[1], 200),
            models.InstrumentAnalytic(self.instrumentIds[2], 300)
        ]

        #   add prices
        self.client.set_analytics(scope, effective_date.year, effective_date.month, effective_date.day, prices)

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
        aggregation = self.client.get_aggregation_by_portfolio(scope, portfolio_id, aggregation_request)

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