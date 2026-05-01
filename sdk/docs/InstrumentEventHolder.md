# InstrumentEventHolder

An instrument event equipped with additional metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | The unique identifier of this corporate action. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The set of identifiers which determine the instrument this event relates to. | 
**lusid_instrument_id** | **str** | The LUID for the instrument. | 
**instrument_scope** | **str** | The scope of the instrument. | 
**description** | **str** | The description of the instrument event. | 
**event_date_range** | [**EventDateRange**](EventDateRange.md) |  | 
**completeness** | **str** | Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete). Available values: Complete, Incomplete. | [optional] [readonly] 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 
**sequence_number** | **int** | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. | [optional] 
**participation_type** | **str** | Indicates the type of participation in this event. Default value: Mandatory. Available values: Mandatory, MandatoryWithChoices, Voluntary. | [optional] [default to 'Mandatory']
**as_at** | **datetime** | The AsAt time of the instrument event, if available. This is a readonly field and should not be provided on upsert. | [optional] [readonly] 
**group_code** | **str** | The group code that determines the processing order of instrument events with the same effective datetime. Available values: Tier1, Tier2, Tier3, Legacy. | [optional] 
## Example

```python
from lusid.models.instrument_event_holder import InstrumentEventHolder
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_event_id: StrictStr = "example_instrument_event_id"
corporate_action_source_id: Optional[ResourceId] = # Replace with your value
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
instrument_scope: StrictStr = "example_instrument_scope"
description: StrictStr = "example_description"
event_date_range: EventDateRange = # Replace with your value
completeness: Optional[StrictStr] = "example_completeness"
instrument_event: InstrumentEvent = # Replace with your value
properties: Optional[List[PerpetualProperty]] = # Replace with your value
sequence_number: Optional[StrictInt] = # Replace with your value
sequence_number: Optional[StrictInt] = None
participation_type: Optional[StrictStr] = "example_participation_type"
as_at: Optional[datetime] = # Replace with your value
group_code: Optional[StrictStr] = "example_group_code"
instrument_event_holder_instance = InstrumentEventHolder(instrument_event_id=instrument_event_id, corporate_action_source_id=corporate_action_source_id, instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, description=description, event_date_range=event_date_range, completeness=completeness, instrument_event=instrument_event, properties=properties, sequence_number=sequence_number, participation_type=participation_type, as_at=as_at, group_code=group_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

