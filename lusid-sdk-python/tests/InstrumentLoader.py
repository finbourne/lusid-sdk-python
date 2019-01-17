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


class InstrumentLoader(object):


    def LoadInstruments(self):

        inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BH4HKS39"))
        inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("BH4HKS3"))

        instrument_definition1 = models.InstrumentDefinition(name="VODAFONE GROUP PLC",
                                                             identifiers={self.FIGI_SCHEME: "BBG000C6K6G9",
                                                                          self.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_1"},
                                                             properties=[inst_isin, inst_sedol])
        # upsert_response = self.client.upsert_instruments({"correlationId1": instrument_definition})

        inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB0031348658"))
        inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("3134865"))

        instrument_definition2 = models.InstrumentDefinition(name="BARCLAYS PLC",
                                                             identifiers={self.FIGI_SCHEME: "BBG000C04D57",
                                                                          self.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_2"},
                                                             properties=[inst_isin, inst_sedol])

        # upsert_response = self.client.upsert_instruments({"correlationId2": instrument_definition})

        inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BDR05C01"))
        inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("BDR05C0"))

        instrument_definition3 = models.InstrumentDefinition(name="NATIONAL GRID PLC",
                                                             identifiers={self.FIGI_SCHEME: "BBG000FV67Q4",
                                                                          self.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_3"},
                                                             properties=[inst_isin, inst_sedol])

        # upsert_response = self.client.upsert_instruments({"correlationId3": instrument_definition})

        inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB00B019KW72"))
        inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("B019KW7"))

        instrument_definition4 = models.InstrumentDefinition(name="SAINSBURY (J) PLC",
                                                             identifiers={self.FIGI_SCHEME: "BBG000BF0KW3",
                                                                          self.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_4"},
                                                             properties=[inst_isin, inst_sedol])

        # upsert_response = self.client.upsert_instruments({"correlationId4": instrument_definition})

        inst_isin = models.InstrumentProperty(self.ISIN_PROPERTY_KEY, models.PropertyValue("GB0008782301"))
        inst_sedol = models.InstrumentProperty(self.SEDOL_PROPERTY_KEY, models.PropertyValue("0878230"))

        instrument_definition5 = models.InstrumentDefinition(name="TAYLOR WIMPEY PLC",
                                                             identifiers={self.FIGI_SCHEME: "BBG000BF4KL1",
                                                                          self.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_5"},
                                                             properties=[inst_isin, inst_sedol])

        upsert_response = self.client.upsert_instruments(
            {
                "correlationId1": instrument_definition1,
                "correlationId2": instrument_definition2,
                "correlationId3": instrument_definition3,
                "correlationId4": instrument_definition4,
                "correlationId5": instrument_definition5
            }
        )

        assert len(upsert_response.values) == 5

        return upsert_response

    def tearDownClass(self):
        inst_list = ["BBG000C6K6G9",
                     "BBG000C04D57",
                     "BBG000FV67Q4",
                     "BBG000BF0KW3",
                     "BBG000BF4KL1",
                     "BBG000BF6B57"]

        for i in inst_list:
            response = cls.client.delete_instrument(cls.FIGI_SCHEME, i)
