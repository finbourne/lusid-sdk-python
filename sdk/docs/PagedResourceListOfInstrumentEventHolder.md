# PagedResourceListOfInstrumentEventHolder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[InstrumentEventHolder]**](InstrumentEventHolder.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_instrument_event_holder import PagedResourceListOfInstrumentEventHolder

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfInstrumentEventHolder from a JSON string
paged_resource_list_of_instrument_event_holder_instance = PagedResourceListOfInstrumentEventHolder.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfInstrumentEventHolder.to_json()

# convert the object into a dict
paged_resource_list_of_instrument_event_holder_dict = paged_resource_list_of_instrument_event_holder_instance.to_dict()
# create an instance of PagedResourceListOfInstrumentEventHolder from a dict
paged_resource_list_of_instrument_event_holder_form_dict = paged_resource_list_of_instrument_event_holder.from_dict(paged_resource_list_of_instrument_event_holder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


