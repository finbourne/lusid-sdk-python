# ApplicableInstrumentEvent

Represents applicable instrument event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**holding_id** | **int** |  | 
**lusid_instrument_id** | **str** |  | 
**instrument_scope** | **str** |  | 
**instrument_type** | **str** |  | 
**instrument_event_type** | **str** |  | 
**instrument_event_id** | **str** |  | 
**generated_event** | [**InstrumentEventHolder**](InstrumentEventHolder.md) |  | [optional] 
**generated_event_diagnostics** | [**GeneratedEventDiagnostics**](GeneratedEventDiagnostics.md) |  | [optional] 
**loaded_event** | [**InstrumentEventHolder**](InstrumentEventHolder.md) |  | [optional] 
**applied_instrument_event_instruction_id** | **str** |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**transaction_diagnostics** | [**TransactionDiagnostics**](TransactionDiagnostics.md) |  | [optional] 
## Example

```python
from lusid.models.applicable_instrument_event import ApplicableInstrumentEvent
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr

portfolio_id: ResourceId = # Replace with your value
holding_id: StrictInt = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
instrument_scope: StrictStr = "example_instrument_scope"
instrument_type: StrictStr = "example_instrument_type"
instrument_event_type: StrictStr = "example_instrument_event_type"
instrument_event_id: StrictStr = "example_instrument_event_id"
generated_event: Optional[InstrumentEventHolder] = # Replace with your value
generated_event_diagnostics: Optional[GeneratedEventDiagnostics] = # Replace with your value
loaded_event: Optional[InstrumentEventHolder] = # Replace with your value
applied_instrument_event_instruction_id: Optional[StrictStr] = "example_applied_instrument_event_instruction_id"
transactions: Optional[conlist(Transaction)] = None
transaction_diagnostics: Optional[TransactionDiagnostics] = # Replace with your value
applicable_instrument_event_instance = ApplicableInstrumentEvent(portfolio_id=portfolio_id, holding_id=holding_id, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, instrument_type=instrument_type, instrument_event_type=instrument_event_type, instrument_event_id=instrument_event_id, generated_event=generated_event, generated_event_diagnostics=generated_event_diagnostics, loaded_event=loaded_event, applied_instrument_event_instruction_id=applied_instrument_event_instruction_id, transactions=transactions, transaction_diagnostics=transaction_diagnostics)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

