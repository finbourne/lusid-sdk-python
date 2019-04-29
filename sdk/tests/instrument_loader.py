from collections import namedtuple

import lusid
import lusid.models as models


class InstrumentLoader:
    __InstrumentSpec = namedtuple("InstrumentSpec", ["Figi", "Name"])

    __instruments = [
        __InstrumentSpec("BBG000C6K6G9", "VODAFONE GROUP PLC"),
        __InstrumentSpec("BBG000C04D57", "BARCLAYS PLC"),
        __InstrumentSpec("BBG000FV67Q4", "NATIONAL GRID PLC"),
        __InstrumentSpec("BBG000BF0KW3", "SAINSBURY (J) PLC"),
        __InstrumentSpec("BBG000BF4KL1", "TAYLOR WIMPEY PLC")
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

        response = self.instruments_api.upsert_instruments(requests=instruments_to_create)

        assert (len(response.failed) == 0)

        return sorted([i.lusid_instrument_id for i in response.values.values()])

    def delete_instruments(self):
        for i in self.__instruments:
            self.instruments_api.delete_instrument("Figi", i.Figi)
