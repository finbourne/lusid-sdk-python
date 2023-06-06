# UpsertSingleStructuredDataResponse

Response from upserting structured data document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | **datetime** | The value that was successfully retrieved. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSingleStructuredDataResponse from a JSON string
upsert_single_structured_data_response_instance = UpsertSingleStructuredDataResponse.from_json(json)
# print the JSON string representation of the object
print UpsertSingleStructuredDataResponse.to_json()

# convert the object into a dict
upsert_single_structured_data_response_dict = upsert_single_structured_data_response_instance.to_dict()
# create an instance of UpsertSingleStructuredDataResponse from a dict
upsert_single_structured_data_response_form_dict = upsert_single_structured_data_response.from_dict(upsert_single_structured_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


