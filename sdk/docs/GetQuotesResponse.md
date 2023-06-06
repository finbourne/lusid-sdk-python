# GetQuotesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Quote]**](Quote.md) | The quotes which have been successfully retrieved. | [optional] 
**not_found** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be found along with a reason why. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be retrieved due to an error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_quotes_response import GetQuotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuotesResponse from a JSON string
get_quotes_response_instance = GetQuotesResponse.from_json(json)
# print the JSON string representation of the object
print GetQuotesResponse.to_json()

# convert the object into a dict
get_quotes_response_dict = get_quotes_response_instance.to_dict()
# create an instance of GetQuotesResponse from a dict
get_quotes_response_form_dict = get_quotes_response.from_dict(get_quotes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


