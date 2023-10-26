# GetDataMapResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, DataMapping]**](DataMapping.md) | The set of values that were successfully retrieved. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The set of values that could not be retrieved along with a reason for this, e.g. badly formed request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_data_map_response import GetDataMapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataMapResponse from a JSON string
get_data_map_response_instance = GetDataMapResponse.from_json(json)
# print the JSON string representation of the object
print GetDataMapResponse.to_json()

# convert the object into a dict
get_data_map_response_dict = get_data_map_response_instance.to_dict()
# create an instance of GetDataMapResponse from a dict
get_data_map_response_form_dict = get_data_map_response.from_dict(get_data_map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


