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

## Example

```python
from lusid.models.instrument_event_instruction_request import InstrumentEventInstructionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEventInstructionRequest from a JSON string
instrument_event_instruction_request_instance = InstrumentEventInstructionRequest.from_json(json)
# print the JSON string representation of the object
print InstrumentEventInstructionRequest.to_json()

# convert the object into a dict
instrument_event_instruction_request_dict = instrument_event_instruction_request_instance.to_dict()
# create an instance of InstrumentEventInstructionRequest from a dict
instrument_event_instruction_request_form_dict = instrument_event_instruction_request.from_dict(instrument_event_instruction_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


