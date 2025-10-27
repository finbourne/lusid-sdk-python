# UpsertInstrumentEventRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | Free string that uniquely identifies the event within the corporate action source | 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The set of identifiers which determine the instrument this event relates to. | 
**description** | **str** | The description of the instrument event. | [optional] 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 
**sequence_number** | **int** | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. | [optional] 
**participation_type** | **str** | Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary. | [optional] [default to 'Mandatory']
**event_date_stamps** | [**Dict[str, YearMonthDay]**](YearMonthDay.md) | The date stamps corresponding to the relevant date-time fields for the instrument event. The key for each provided date stamp must match the field name of a valid datetime field from the InstrumentEvent DTO. | [optional] 
## Example

```python
from lusid.models.upsert_instrument_event_request import UpsertInstrumentEventRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_event_id: StrictStr = "example_instrument_event_id"
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
description: Optional[StrictStr] = "example_description"
instrument_event: InstrumentEvent = # Replace with your value
properties: Optional[List[PerpetualProperty]] = # Replace with your value
sequence_number: Optional[StrictInt] = # Replace with your value
sequence_number: Optional[StrictInt] = None
participation_type: Optional[StrictStr] = "example_participation_type"
event_date_stamps: Optional[Dict[str, YearMonthDay]] = # Replace with your value
upsert_instrument_event_request_instance = UpsertInstrumentEventRequest(instrument_event_id=instrument_event_id, instrument_identifiers=instrument_identifiers, description=description, instrument_event=instrument_event, properties=properties, sequence_number=sequence_number, participation_type=participation_type, event_date_stamps=event_date_stamps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

