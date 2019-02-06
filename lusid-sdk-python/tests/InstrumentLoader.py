import lusid.models as models

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class InstrumentLoader(object):

    inst_list = ["BBG000C6K6G9",
                 "BBG000C04D57",
                 "BBG000FV67Q4",
                 "BBG000BF0KW3",
                 "BBG000BF4KL1"]

    ISIN_PROPERTY_KEY = "Instrument/default/Isin"
    SEDOL_PROPERTY_KEY = "Instrument/default/Sedol"
    FIGI_SCHEME = "Figi"
    CUSTOM_INTERNAL_SCHEME = "ClientInternal"

    @classmethod
    def load_instruments(cls, client):

        isin_vod = models.InstrumentProperty(InstrumentLoader.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BH4HKS39"))
        sedol_vod = models.InstrumentProperty(InstrumentLoader.SEDOL_PROPERTY_KEY, models.PropertyValue("BH4HKS3"))

        instrument_definition1 = models.InstrumentDefinition(name="VODAFONE GROUP PLC",
                                                             identifiers={InstrumentLoader.FIGI_SCHEME: "BBG000C6K6G9",
                                                                          InstrumentLoader.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_1"},
                                                             properties=[isin_vod, sedol_vod])

        isin_barc = models.InstrumentProperty(InstrumentLoader.ISIN_PROPERTY_KEY, models.PropertyValue("GB0031348658"))
        sedol_barc = models.InstrumentProperty(InstrumentLoader.SEDOL_PROPERTY_KEY, models.PropertyValue("3134865"))

        instrument_definition2 = models.InstrumentDefinition(name="BARCLAYS PLC",
                                                             identifiers={InstrumentLoader.FIGI_SCHEME: "BBG000C04D57",
                                                                          InstrumentLoader.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_2"},
                                                             properties=[isin_barc, sedol_barc])

        isin_grid = models.InstrumentProperty(InstrumentLoader.ISIN_PROPERTY_KEY, models.PropertyValue("GB00BDR05C01"))
        sedol_grid = models.InstrumentProperty(InstrumentLoader.SEDOL_PROPERTY_KEY, models.PropertyValue("BDR05C0"))

        instrument_definition3 = models.InstrumentDefinition(name="NATIONAL GRID PLC",
                                                             identifiers={InstrumentLoader.FIGI_SCHEME: "BBG000FV67Q4",
                                                                          InstrumentLoader.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_3"},
                                                             properties=[isin_grid, sedol_grid])

        isin_sains = models.InstrumentProperty(InstrumentLoader.ISIN_PROPERTY_KEY, models.PropertyValue("GB00B019KW72"))
        sedol_sains = models.InstrumentProperty(InstrumentLoader.SEDOL_PROPERTY_KEY, models.PropertyValue("B019KW7"))

        instrument_definition4 = models.InstrumentDefinition(name="SAINSBURY (J) PLC",
                                                             identifiers={InstrumentLoader.FIGI_SCHEME: "BBG000BF0KW3",
                                                                          InstrumentLoader.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_4"},
                                                             properties=[isin_sains, sedol_sains])

        isin_tayl = models.InstrumentProperty(InstrumentLoader.ISIN_PROPERTY_KEY, models.PropertyValue("GB0008782301"))
        sedol_tayl = models.InstrumentProperty(InstrumentLoader.SEDOL_PROPERTY_KEY, models.PropertyValue("0878230"))

        instrument_definition5 = models.InstrumentDefinition(name="TAYLOR WIMPEY PLC",
                                                             identifiers={InstrumentLoader.FIGI_SCHEME: "BBG000BF4KL1",
                                                                          InstrumentLoader.CUSTOM_INTERNAL_SCHEME: "INTERNAL_ID_5"},
                                                             properties=[isin_tayl, sedol_tayl])

        upsert_response = client.upsert_instruments(
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

    @classmethod
    def delete_instruments(cls, client):

        for i in InstrumentLoader.inst_list:
            response = client.delete_instrument(InstrumentLoader.FIGI_SCHEME, i)
