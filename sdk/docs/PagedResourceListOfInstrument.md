# PagedResourceListOfInstrument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Instrument]**](Instrument.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_instrument import PagedResourceListOfInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfInstrument from a JSON string
paged_resource_list_of_instrument_instance = PagedResourceListOfInstrument.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfInstrument.to_json()

# convert the object into a dict
paged_resource_list_of_instrument_dict = paged_resource_list_of_instrument_instance.to_dict()
# create an instance of PagedResourceListOfInstrument from a dict
paged_resource_list_of_instrument_form_dict = paged_resource_list_of_instrument.from_dict(paged_resource_list_of_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


