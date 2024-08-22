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
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_event_instruction import InstrumentEventInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEventInstruction from a JSON string
instrument_event_instruction_instance = InstrumentEventInstruction.from_json(json)
# print the JSON string representation of the object
print InstrumentEventInstruction.to_json()

# convert the object into a dict
instrument_event_instruction_dict = instrument_event_instruction_instance.to_dict()
# create an instance of InstrumentEventInstruction from a dict
instrument_event_instruction_form_dict = instrument_event_instruction.from_dict(instrument_event_instruction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


