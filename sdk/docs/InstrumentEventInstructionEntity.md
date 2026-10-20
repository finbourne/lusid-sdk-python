# InstrumentEventInstructionEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_unique_id** | **str** | The unique id of the entity. | 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**status** | **str** | The status of the entity at the current time. Available values: Prevailing, Deleted, DoesNotExist. | 
**as_at_deleted** | **datetime** | The asAt datetime at which the entity was deleted. | [optional] 
**user_id_deleted** | **str** | The unique id of the user who deleted the entity. | [optional] 
**request_id_deleted** | **str** | The unique request id of the command that deleted the entity. | [optional] 
**prevailing_instrument_event_instruction** | [**InstrumentEventInstruction**](InstrumentEventInstruction.md) |  | [optional] 
**deleted_instrument_event_instruction** | [**InstrumentEventInstruction**](InstrumentEventInstruction.md) |  | [optional] 
**previewed_status** | **str** | The status of the previewed entity. Available values: Prevailing, Deleted, DoesNotExist. | [optional] 
**previewed_instrument_event_instruction** | [**InstrumentEventInstruction**](InstrumentEventInstruction.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_event_instruction_entity import InstrumentEventInstructionEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: StrictStr = "example_href"
entity_unique_id: StrictStr = "example_entity_unique_id"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
status: StrictStr = "example_status"
as_at_deleted: Optional[datetime] = # Replace with your value
user_id_deleted: Optional[StrictStr] = "example_user_id_deleted"
request_id_deleted: Optional[StrictStr] = "example_request_id_deleted"
prevailing_instrument_event_instruction: Optional[InstrumentEventInstruction] = # Replace with your value
deleted_instrument_event_instruction: Optional[InstrumentEventInstruction] = # Replace with your value
previewed_status: Optional[StrictStr] = "example_previewed_status"
previewed_instrument_event_instruction: Optional[InstrumentEventInstruction] = # Replace with your value
links: Optional[List[Link]] = None
instrument_event_instruction_entity_instance = InstrumentEventInstructionEntity(href=href, entity_unique_id=entity_unique_id, as_at_version_number=as_at_version_number, status=status, as_at_deleted=as_at_deleted, user_id_deleted=user_id_deleted, request_id_deleted=request_id_deleted, prevailing_instrument_event_instruction=prevailing_instrument_event_instruction, deleted_instrument_event_instruction=deleted_instrument_event_instruction, previewed_status=previewed_status, previewed_instrument_event_instruction=previewed_instrument_event_instruction, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

