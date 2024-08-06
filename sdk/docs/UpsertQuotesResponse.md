# UpsertQuotesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Quote]**](Quote.md) | The quotes which have been successfully updated or inserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be updated or inserted along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_quotes_response import UpsertQuotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertQuotesResponse from a JSON string
upsert_quotes_response_instance = UpsertQuotesResponse.from_json(json)
# print the JSON string representation of the object
print UpsertQuotesResponse.to_json()

# convert the object into a dict
upsert_quotes_response_dict = upsert_quotes_response_instance.to_dict()
# create an instance of UpsertQuotesResponse from a dict
upsert_quotes_response_form_dict = upsert_quotes_response.from_dict(upsert_quotes_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


