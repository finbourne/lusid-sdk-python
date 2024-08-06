# GetStructuredResultDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, StructuredResultData]**](StructuredResultData.md) | The set of values that were successfully retrieved. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_structured_result_data_response import GetStructuredResultDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStructuredResultDataResponse from a JSON string
get_structured_result_data_response_instance = GetStructuredResultDataResponse.from_json(json)
# print the JSON string representation of the object
print GetStructuredResultDataResponse.to_json()

# convert the object into a dict
get_structured_result_data_response_dict = get_structured_result_data_response_instance.to_dict()
# create an instance of GetStructuredResultDataResponse from a dict
get_structured_result_data_response_form_dict = get_structured_result_data_response.from_dict(get_structured_result_data_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


