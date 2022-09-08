from collections import namedtuple

import lusid
import lusid.models as models


class InstrumentLoader:
    __InstrumentSpec = namedtuple("InstrumentSpec", ["Figi", "Name"])

    __instruments = [
        __InstrumentSpec("BBG00KTDTF73", "AT&T INC"),
        __InstrumentSpec("BBG00Y271826", "BYTES TECHNOLOGY GROUP PLC"),
        __InstrumentSpec("BBG00L7XVNP1", "CUSHMAN & WAKEFIELD PLC"),
        __InstrumentSpec("BBG005D5KGM0", "FIRST CITRUS BANCORPORATION"),
        __InstrumentSpec("BBG000DPM932", "FRASERS GROUP PLC")
    ]

    def __init__(self, instruments_api: lusid.InstrumentsApi):
        self.instruments_api = instruments_api

    def load_instruments(self):
        instruments_to_create = {
            i.Figi: models.InstrumentDefinition(
                name=i.Name,
                identifiers={
                    "Figi": models.InstrumentIdValue(value=i.Figi)
                }
            ) for i in self.__instruments
        }

        response = self.instruments_api.upsert_instruments(request_body=instruments_to_create)

        assert (len(response.failed) == 0)

        return sorted([i.lusid_instrument_id for i in response.values.values()])

    def delete_instruments(self):
        for i in self.__instruments:
            self.instruments_api.delete_instrument("Figi", i.Figi)
