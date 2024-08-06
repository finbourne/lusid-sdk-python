# PagedResourceListOfInstrumentEventInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[InstrumentEventInstruction]**](InstrumentEventInstruction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_instrument_event_instruction import PagedResourceListOfInstrumentEventInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfInstrumentEventInstruction from a JSON string
paged_resource_list_of_instrument_event_instruction_instance = PagedResourceListOfInstrumentEventInstruction.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfInstrumentEventInstruction.to_json()

# convert the object into a dict
paged_resource_list_of_instrument_event_instruction_dict = paged_resource_list_of_instrument_event_instruction_instance.to_dict()
# create an instance of PagedResourceListOfInstrumentEventInstruction from a dict
paged_resource_list_of_instrument_event_instruction_form_dict = paged_resource_list_of_instrument_event_instruction.from_dict(paged_resource_list_of_instrument_event_instruction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


