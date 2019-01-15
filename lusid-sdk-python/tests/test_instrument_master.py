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

        cls.ISIN_PROPERTY_KEY = "Instrument/default/Isin"
        cls.SEDOL_PROPERTY_KEY = "Instrument/default/Sedol"
        cls.FIGI_SCHEME = "Figi"
        cls.CUSTOM_INTERNAL_SCHEME = "ClientInternal"

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

        response = cls.seed_instruments()

    @classmethod
    def tearDownClass(cls):
        inst_list = ["BBG000C6K6G9",
                     "BBG000C04D57",
                     "BBG000FV67Q4",
                     "BBG000BF0KW3",
                     "BBG000BF4KL1",
                     "BBG000BF6B57"]

        for i in inst_list:
            response = cls.client.delete_instrument(cls.FIGI_SCHEME, i)
        # fbn_figi = cls.client.get_instrument("Figi", "BBG000C6K6G9")
        print("JKH")
    @classmethod
    def seed_instruments(cls):

        inst_isin = models.InstrumentProperty(cls.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BH4HKS39"))
        inst_sedol = models.InstrumentProperty(cls.SEDOL_PROPERTY_KEY, models.PropertyValue("BH4HKS3"))

        instrument_definition1 = models.InstrumentDefinition(name="VODAFONE GROUP PLC",
                                                            identifiers={cls.FIGI_SCHEME: "BBG000C6K6G9",
                                                                         cls.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_1"},
                                                            properties=[inst_isin, inst_sedol])
        # upsert_response = cls.client.upsert_instruments({"correlationId1": instrument_definition})


        inst_isin = models.InstrumentProperty(cls.ISIN_PROPERTY_KEY, models.PropertyValue("GB0031348658"))
        inst_sedol = models.InstrumentProperty(cls.SEDOL_PROPERTY_KEY, models.PropertyValue("3134865"))

        instrument_definition2 = models.InstrumentDefinition(name="BARCLAYS PLC",
                                                            identifiers={cls.FIGI_SCHEME: "BBG000C04D57",
                                                                         cls.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_2"},
                                                            properties=[inst_isin, inst_sedol])

        # upsert_response = cls.client.upsert_instruments({"correlationId2": instrument_definition})

        inst_isin = models.InstrumentProperty(cls.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BDR05C01"))
        inst_sedol = models.InstrumentProperty(cls.SEDOL_PROPERTY_KEY, models.PropertyValue("BDR05C0"))

        instrument_definition3 = models.InstrumentDefinition(name="NATIONAL GRID PLC",
                                                            identifiers={cls.FIGI_SCHEME: "BBG000FV67Q4",
                                                                         cls.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_3"},
                                                            properties=[inst_isin, inst_sedol])

        # upsert_response = cls.client.upsert_instruments({"correlationId3": instrument_definition})

        inst_isin = models.InstrumentProperty(cls.ISIN_PROPERTY_KEY, models.PropertyValue("GB00B019KW72"))
        inst_sedol = models.InstrumentProperty(cls.SEDOL_PROPERTY_KEY, models.PropertyValue("B019KW7"))

        instrument_definition4 = models.InstrumentDefinition(name="SAINSBURY (J) PLC",
                                                            identifiers={cls.FIGI_SCHEME: "BBG000BF0KW3",
                                                                         cls.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_4"},
                                                            properties=[inst_isin, inst_sedol])

        # upsert_response = cls.client.upsert_instruments({"correlationId4": instrument_definition})

        inst_isin = models.InstrumentProperty(cls.ISIN_PROPERTY_KEY, models.PropertyValue("GB0008782301"))
        inst_sedol = models.InstrumentProperty(cls.SEDOL_PROPERTY_KEY, models.PropertyValue("0878230"))

        instrument_definition5 = models.InstrumentDefinition(name="TAYLOR WIMPEY PLC",
                                                            identifiers={cls.FIGI_SCHEME: "BBG000BF4KL1",
                                                                         cls.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_5"},
                                                            properties=[inst_isin, inst_sedol])

        upsert_response = cls.client.upsert_instruments(
            {
                "correlationId1": instrument_definition1,
                "correlationId2": instrument_definition2,
                "correlationId3": instrument_definition3,
                "correlationId4": instrument_definition4,
                "correlationId5": instrument_definition5
            }
        )

        assert len(upsert_response.values) == 5


    def test_lookup_instrument_by_unique_id(self):

        # Look up an instrument that already exists in the instrument master by a
        # unique id, in this case an OpenFigi, and also return a list of aliases

        fbn_ids = self.client.get_instruments(self.FIGI_SCHEME, ["BBG000C6K6G9", "BBG000BF4KL1"],
                                              instrument_property_keys=[self.ISIN_PROPERTY_KEY,
                                                                        self.SEDOL_PROPERTY_KEY])

        self.assertEqual(fbn_ids.values["BBG000C6K6G9"].name, "VODAFONE GROUP PLC")

        # get instrument from the master
        fbn_inst = fbn_ids.values["BBG000C6K6G9"]
        #fbn_inst = self.client.get_instrument(self.FIGI_SCHEME, "BBG000C6K6G9")
        assert fbn_inst.name == "VODAFONE GROUP PLC"

        # get isin
        assert fbn_ids.values["BBG000C6K6G9"].properties[0].key == self.ISIN_PROPERTY_KEY
        assert fbn_ids.values["BBG000C6K6G9"].properties[0].value == "GB00BH4HKS39"

        assert fbn_ids.values["BBG000C6K6G9"].properties[1].key == self.SEDOL_PROPERTY_KEY
        assert fbn_ids.values["BBG000C6K6G9"].properties[1].value == "BH4HKS3"



    def test_lookup_instrument_by_market_identifier(self):

        # Look up instruments that already exists in the instrument master by a
        # list of market identifiers...Sedol and Isin.
        # inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BH4HKS39"))
        # inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("B019KW7"))
        fbn_inst = self.client.find_instruments([models.Property(self.ISIN_PROPERTY_KEY,
                                                                           "GB00BH4HKS39"),
                                                 models.Property(self.ISIN_PROPERTY_KEY,
                                                                           "GB0031348658"),
                                                 models.Property(self.ISIN_PROPERTY_KEY,
                                                                           "GB00BDR05C01"),
                                                 models.Property(self.SEDOL_PROPERTY_KEY,
                                                                           "B019KW7"),
                                                 models.Property(self.SEDOL_PROPERTY_KEY,
                                                                           "0878230")])

        # self.assertGreaterEqual(len(fbn_inst.values), 5)
        # we expect 5 or more results (if other instruments are present, but each FIGI should be present in
        # the return list, and should match the 5 original instruments

        # Compare returned list to seed instruments Figis

        inst_list = ["BBG000C6K6G9",
                     "BBG000C04D57",
                     "BBG000FV67Q4",
                     "BBG000BF0KW3",
                     "BBG000BF4KL1"]

        # get returned Figi list
        found_figis = [item.identifiers['Figi'] for item in fbn_inst.values if 'Figi' in item.identifiers]
        assert len(found_figis) ==5
        # returned instrument list (found_figis) should not contain instruments that are missing from inst_list
        not_found = [item for item in inst_list if item not in found_figis]

        assert len(not_found) == 0


    def test_find_non_mastered_instrument_from_external_source(self):

        # Look up an instrument not currently in the instrument master (WPP LN)

        matched_ids = self.client.match_instruments(self.FIGI_SCHEME, ["BBG000BF6B57"])

        self.assertEqual(len(matched_ids.values["BBG000BF6B57"]), 1)

        instrument_definition = matched_ids.values["BBG000BF6B57"][0]

        # Add the instrument to the instrument master.  The result of the match contains
        # the required information to master the instrument e.g. name, identifier, market
        # identifier alias etc.

        upsert_response = self.client.upsert_instruments({"correlationId6": instrument_definition})

        # get instrument from the master
        fbn_inst = self.client.get_instrument(self.FIGI_SCHEME, "BBG000BF6B57")

        assert fbn_inst.identifiers[self.FIGI_SCHEME] == "BBG000BF6B57"
        assert fbn_inst.name == "WPP PLC"



if __name__ == '__main__':
    unittest.main()

