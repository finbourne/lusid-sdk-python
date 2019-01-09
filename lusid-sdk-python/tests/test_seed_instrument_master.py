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

    def test_seed_instruments(self):

        instrument_definition = models.InstrumentDefinition(name="VODAFONE GROUP PLC",
                                                            identifiers={"Figi": "BBG000C6K6G9",
                                                                         "ClientInternal": "INTERNAL_ID_1"})

        upsert_response = self.client.upsert_instruments({"correlationId1": instrument_definition})

        instrument_definition = models.InstrumentDefinition(name="BARCLAYS PLC",
                                                            identifiers={"Figi": "BBG000C04D57",
                                                                         "ClientInternal": "INTERNAL_ID_2"})

        upsert_response = self.client.upsert_instruments({"correlationId2": instrument_definition})

        instrument_definition = models.InstrumentDefinition(name="NATIONAL GRID PLC",
                                                            identifiers={"Figi": "BBG000FV67Q4",
                                                                         "ClientInternal": "INTERNAL_ID_3"})

        upsert_response = self.client.upsert_instruments({"correlationId3": instrument_definition})

        instrument_definition = models.InstrumentDefinition(name="SAINSBURY (J) PLC",
                                                            identifiers={"Figi": "BBG000BF0KW3",
                                                                         "ClientInternal": "INTERNAL_ID_4"})

        upsert_response = self.client.upsert_instruments({"correlationId4": instrument_definition})

        instrument_definition = models.InstrumentDefinition(name="TAYLOR WIMPEY PLC",
                                                            identifiers={"Figi": "BBG000BF4KL1",
                                                                         "ClientInternal": "INTERNAL_ID_5"})

        upsert_response = self.client.upsert_instruments({"correlationId5": instrument_definition})

        assert len(upsert_response.values) == 1

    def test_lookup_instrument_by_unique_id(self):
        # Look up an instrument that already exists in the instrument master by a
        # unique id, in this case an OpenFigi, and also return a list of aliases
        fbn_ids = self.client.get_instruments("Figi", ["BBG000BF0KW3"])

        # assertThat(lookedUpInstruments.getValues(), hasKey("BBG000BF0KW3"));
        self.assertEquals(fbn_ids.values["BBG000BF0KW3"].name, "SAINSBURY (J) PLC")

        fbn_inst = self.client.get_instrument("Figi", "BBG000BF0KW3")
        # now check the key is as expected???
        # next check the properties have gone in as expected...Sedol and Isin

        #assert fbn_inst("BBG000BF0KW3")=="SAINSBURY (J) PLC"

    def test_lookup_instrument_by_market_identifier(self):

        # Look up instruments that already exists in the instrument master by a
        # list of market identifiers...Sedol and Isin.
        print("placeholder")

    def test_find_non_mastered_instrument_from_external_source(self):

        # Look up an instrument not currently in the instrument master (WPP LN)

        matched_ids = self.client.match_instruments("Figi", ["BBG000BF6B57"])
        self.assertEqual(matched_ids.values["BBG000BF6B57"][0].name, "WPP PLC")
        # Add the instrument to the instrument master. Can we do this from FIGI, ShareclassFigi, Ticker?



    @classmethod
    def seed_instruments(self):

        print("this doesnt run?")


if __name__ == '__main__':
    unittest.main()
