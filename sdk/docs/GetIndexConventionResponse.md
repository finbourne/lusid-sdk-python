# GetIndexConventionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers that did not resolve to a conventions along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_index_convention_response import GetIndexConventionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexConventionResponse from a JSON string
get_index_convention_response_instance = GetIndexConventionResponse.from_json(json)
# print the JSON string representation of the object
print GetIndexConventionResponse.to_json()

# convert the object into a dict
get_index_convention_response_dict = get_index_convention_response_instance.to_dict()
# create an instance of GetIndexConventionResponse from a dict
get_index_convention_response_form_dict = get_index_convention_response.from_dict(get_index_convention_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


