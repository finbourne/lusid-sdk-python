import unittest

import lusid
import lusid.models as models
from lusidfeature import lusid_feature
from lusid.utilities.api_client_builder import ApiClientBuilder
from lusid.exceptions import ApiException
from utilities import TestDataUtilities


class Instruments(unittest.TestCase):
    property_definitions_api = None

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        cls.instruments_api = lusid.InstrumentsApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)

    @classmethod
    def ensure_property_definition(cls, code):

        try:
            cls.property_definitions_api.get_property_definition(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                code=code
            )
        except ApiException as e:
            # property definition doesn't exist (returns 404), so create one
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                life_time="Perpetual",
                code=code,
                value_required=False,
                data_type_id=models.ResourceId("system", "string")
            )

            # create the property
            cls.property_definitions_api.create_property_definition(definition=property_definition)

    @lusid_feature("F5-4")
    def test_seed_instrument_master(self):
        response = self.instruments_api.upsert_instruments(requests={

            "BBG000FD8G46": models.InstrumentDefinition(
                name="HISCOX LTD",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000FD8G46"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1")
                }
            ),

            "BBG000DW76R4": models.InstrumentDefinition(
                name="ITV PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000DW76R4"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_2")
                }
            ),

            "BBG000PQKVN8": models.InstrumentDefinition(
                name="MONDI PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000PQKVN8"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_3")
                }
            ),

            "BBG000BDWPY0": models.InstrumentDefinition(
                name="NEXT PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000BDWPY0"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_4")
                }
            ),

            "BBG000BF46Y8": models.InstrumentDefinition(
                name="TESCO PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000BF46Y8"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_5")
                }
            )
        })

        self.assertEqual(len(response.values), 5, response.failed)

    @lusid_feature("F21-1")
    def test_lookup_instrument_by_unique_id(self):

        figi = "BBG000FD8G46"

        # set up the instrument
        response = self.instruments_api.upsert_instruments(requests={
            figi: models.InstrumentDefinition(
                name="HISCOX LTD",
                identifiers={
                    "Figi": models.InstrumentIdValue(value=figi),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1")
                }
            )
        })
        self.assertEqual(len(response.values), 1, response.failed)

        # look up an instrument that already exists in the instrument master by a
        # unique id, in this case an OpenFigi, and also return a list of aliases
        looked_up_instruments = self.instruments_api.get_instruments(identifier_type="Figi",
                                                                     identifiers=[figi],
                                                                     instrument_property_keys=[
                                                                         "Instrument/default/ClientInternal"
                                                                     ])

        self.assertTrue(figi in looked_up_instruments.values, msg=f"cannot find {figi}")

        instrument = looked_up_instruments.values[figi]
        self.assertTrue(instrument.name, "HISCOX LTD")

        property = next(filter(lambda i: i.key == "Instrument/default/ClientInternal", instrument.properties), None)
        self.assertTrue(property.value, "internal_id_1")

    @lusid_feature("F21-1")
    def test_list_available_identifiers(self):

        identifiers = self.instruments_api.get_instrument_identifiers()

        for scheme in identifiers.values:
            print(
                f"name: {scheme.id_name}\nproperty key: {scheme.property_key_value}\nis unique: {scheme.is_unique_identifier}\n")

    @lusid_feature("F21-3")
    def test_list_all_instruments(self):

        page_size = 5

        # list the instruments, restricting the number that are returned
        instruments = self.instruments_api.list_instruments(limit=page_size)

        self.assertLessEqual(len(instruments.values), page_size)

    @lusid_feature("F21-4")
    def test_list_instruments_by_identifier_type(self):

        figis = ["BBG000FD8G46", "BBG000DW76R4", "BBG000PQKVN8"]

        # get a set of instruments querying by FIGIs
        instruments = self.instruments_api.get_instruments(identifier_type="Figi", identifiers=figis)

        for figi in figis:
            self.assertTrue(figi in instruments.values, msg=f"{figi} not returned")

    @lusid_feature("F4-4")
    def test_edit_instrument_property(self):

        property_value = models.PropertyValue(label_value="Insurance")
        property_key = f"Instrument/{TestDataUtilities.tutorials_scope}/CustomSector"
        identifier_type = "Figi"
        identifier = "BBG000FD8G46"

        # update the property
        self.instruments_api.upsert_instruments_properties(instrument_properties=[
            models.UpsertInstrumentPropertyRequest(
                identifier_type=identifier_type,
                identifier=identifier,
                properties=[models.ModelProperty(key=property_key, value=property_value)]
            )
        ])

        # get the instrument with value
        instrument = self.instruments_api.get_instrument(
            identifier_type=identifier_type,
            identifier=identifier,
            instrument_property_keys=[property_key]
        )

        self.assertGreaterEqual(len(instrument.properties), 1)

        prop = list(
            filter(lambda p: p.key == property_key and p.value.label_value == property_value.label_value, instrument.properties))

        self.assertEqual(len(prop), 1, f"cannot find property key=${property_key} value={property_value}")
