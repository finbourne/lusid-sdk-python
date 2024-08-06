# ResourceListOfInstrumentEventHolder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[InstrumentEventHolder]**](InstrumentEventHolder.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_instrument_event_holder import ResourceListOfInstrumentEventHolder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfInstrumentEventHolder from a JSON string
resource_list_of_instrument_event_holder_instance = ResourceListOfInstrumentEventHolder.from_json(json)
# print the JSON string representation of the object
print ResourceListOfInstrumentEventHolder.to_json()

# convert the object into a dict
resource_list_of_instrument_event_holder_dict = resource_list_of_instrument_event_holder_instance.to_dict()
# create an instance of ResourceListOfInstrumentEventHolder from a dict
resource_list_of_instrument_event_holder_form_dict = resource_list_of_instrument_event_holder.from_dict(resource_list_of_instrument_event_holder_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


