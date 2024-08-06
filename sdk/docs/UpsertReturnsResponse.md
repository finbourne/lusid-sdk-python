# UpsertReturnsResponse

Response from upserting Returns

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **List[Dict[str, datetime]]** | The set of values that were successfully retrieved. | [optional] 
**failed** | **List[Dict[str, ErrorDetail]]** | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_returns_response import UpsertReturnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReturnsResponse from a JSON string
upsert_returns_response_instance = UpsertReturnsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertReturnsResponse.to_json()

# convert the object into a dict
upsert_returns_response_dict = upsert_returns_response_instance.to_dict()
# create an instance of UpsertReturnsResponse from a dict
upsert_returns_response_form_dict = upsert_returns_response.from_dict(upsert_returns_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


