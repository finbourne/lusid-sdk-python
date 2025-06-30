# InstrumentEventInstruction

An instruction for an instrument event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_instruction_id** | **str** | The unique identifier for this instruction | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_event_id** | **str** | The identifier of the instrument event being instructed | [optional] 
**instruction_type** | **str** | The type of instruction (Ignore, ElectForPortfolio, ElectForHolding) | [optional] 
**election_key** | **str** | For elected instructions, the key to be chosen | [optional] 
**holding_id** | **int** | For holding instructions, the id of the holding for which the instruction will apply | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The uri for this version of this instruction | [optional] 
**entitlement_date_instructed** | **datetime** | The instructed entitlement date for the event (where none is set on the event itself) | [optional] 
**quantity_instructed** | [**QuantityInstructed**](QuantityInstructed.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_event_instruction import InstrumentEventInstruction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
instrument_event_instruction_id: Optional[StrictStr] = "example_instrument_event_instruction_id"
portfolio_id: Optional[ResourceId] = # Replace with your value
instrument_event_id: Optional[StrictStr] = "example_instrument_event_id"
instruction_type: Optional[StrictStr] = "example_instruction_type"
election_key: Optional[StrictStr] = "example_election_key"
holding_id: Optional[StrictInt] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
entitlement_date_instructed: Optional[datetime] = # Replace with your value
quantity_instructed: Optional[QuantityInstructed] = # Replace with your value
links: Optional[conlist(Link)] = None
instrument_event_instruction_instance = InstrumentEventInstruction(instrument_event_instruction_id=instrument_event_instruction_id, portfolio_id=portfolio_id, instrument_event_id=instrument_event_id, instruction_type=instruction_type, election_key=election_key, holding_id=holding_id, version=version, href=href, entitlement_date_instructed=entitlement_date_instructed, quantity_instructed=quantity_instructed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

