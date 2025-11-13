# InstrumentEventInstruction

An instruction for an instrument event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_instruction_id** | **str** | The unique identifier for this instruction | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_event_id** | **str** | The identifier of the instrument event being instructed | [optional] 
**instruction_type** | **str** | The type of instruction (Ignore, ElectForPortfolio, ElectForHolding, ElectForLoanFacilityHolding) | [optional] 
**election_key** | **str** | For elected instructions, the key to be chosen | [optional] 
**holding_id** | **int** | For holding instructions, the id of the holding for which the instruction will apply | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The uri for this version of this instruction | [optional] 
**entitlement_date_instructed** | **datetime** | The instructed entitlement date for the event (where none is set on the event itself) | [optional] 
**quantity_instructed** | [**QuantityInstructed**](QuantityInstructed.md) |  | [optional] 
**tax_lot_id** | **str** | For loan facility holding instructions, the tax lot id of the holding for which the instruction will apply | [optional] 
**ignore_cost_impact** | **bool** | For loan facility holding instructions, set this flag to &#39;true&#39; if you want the event to not impact cost. If you want to use this option, do not add multiple instructions to the same tax lot or you will get undefined behaviour. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_event_instruction import InstrumentEventInstruction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
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
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
ignore_cost_impact: Optional[StrictBool] = # Replace with your value
ignore_cost_impact:Optional[StrictBool] = None
links: Optional[List[Link]] = None
instrument_event_instruction_instance = InstrumentEventInstruction(instrument_event_instruction_id=instrument_event_instruction_id, portfolio_id=portfolio_id, instrument_event_id=instrument_event_id, instruction_type=instruction_type, election_key=election_key, holding_id=holding_id, version=version, href=href, entitlement_date_instructed=entitlement_date_instructed, quantity_instructed=quantity_instructed, tax_lot_id=tax_lot_id, ignore_cost_impact=ignore_cost_impact, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

