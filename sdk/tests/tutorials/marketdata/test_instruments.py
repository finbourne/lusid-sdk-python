import unittest

import lusid
import lusid.models as models
from lusid.utilities.api_client_builder import ApiClientBuilder
from utilities.credentials_source import CredentialsSource


class Instruments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = ApiClientBuilder().build(CredentialsSource.secrets_path())

        cls.instruments_api = lusid.InstrumentsApi(api_client)

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