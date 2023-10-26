# DeleteInstrumentPropertiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The as-at datetime at which properties were deleted. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.delete_instrument_properties_response import DeleteInstrumentPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInstrumentPropertiesResponse from a JSON string
delete_instrument_properties_response_instance = DeleteInstrumentPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print DeleteInstrumentPropertiesResponse.to_json()

# convert the object into a dict
delete_instrument_properties_response_dict = delete_instrument_properties_response_instance.to_dict()
# create an instance of DeleteInstrumentPropertiesResponse from a dict
delete_instrument_properties_response_form_dict = delete_instrument_properties_response.from_dict(delete_instrument_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


