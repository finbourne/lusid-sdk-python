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
**applied_instrument_event_instruction_id** | **str** |  | 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**transaction_diagnostics** | [**TransactionDiagnostics**](TransactionDiagnostics.md) |  | [optional] 

## Example

```python
from lusid.models.applicable_instrument_event import ApplicableInstrumentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicableInstrumentEvent from a JSON string
applicable_instrument_event_instance = ApplicableInstrumentEvent.from_json(json)
# print the JSON string representation of the object
print ApplicableInstrumentEvent.to_json()

# convert the object into a dict
applicable_instrument_event_dict = applicable_instrument_event_instance.to_dict()
# create an instance of ApplicableInstrumentEvent from a dict
applicable_instrument_event_form_dict = applicable_instrument_event.from_dict(applicable_instrument_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


