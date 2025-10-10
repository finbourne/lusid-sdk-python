# InstrumentEventInstructionRequest

The request to create an instruction for an instrument event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_instruction_id** | **str** | The unique identifier for this instruction | 
**instrument_event_id** | **str** | The identifier of the instrument event being instructed | 
**instruction_type** | **str** | The type of instruction (Ignore, ElectForPortfolio, ElectForHolding) | 
**election_key** | **str** | For elected instructions, the key to be chosen | [optional] 
**holding_id** | **int** | For holding instructions, the id of the holding for which the instruction will apply | [optional] 
**entitlement_date_instructed** | **datetime** | The instructed entitlement date for the event (where none is set on the event itself) | [optional] 
**quantity_instructed** | [**QuantityInstructed**](QuantityInstructed.md) |  | [optional] 
**tax_lot_id** | **str** | For loan facility holding instructions, the tax lot id of the holding for which the instruction will apply | [optional] 
## Example

```python
from lusid.models.instrument_event_instruction_request import InstrumentEventInstructionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, constr
from datetime import datetime
instrument_event_instruction_id: StrictStr = "example_instrument_event_instruction_id"
instrument_event_id: StrictStr = "example_instrument_event_id"
instruction_type: StrictStr = "example_instruction_type"
election_key: Optional[StrictStr] = "example_election_key"
holding_id: Optional[StrictInt] = # Replace with your value
entitlement_date_instructed: Optional[datetime] = # Replace with your value
quantity_instructed: Optional[QuantityInstructed] = # Replace with your value
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
instrument_event_instruction_request_instance = InstrumentEventInstructionRequest(instrument_event_instruction_id=instrument_event_instruction_id, instrument_event_id=instrument_event_id, instruction_type=instruction_type, election_key=election_key, holding_id=holding_id, entitlement_date_instructed=entitlement_date_instructed, quantity_instructed=quantity_instructed, tax_lot_id=tax_lot_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

