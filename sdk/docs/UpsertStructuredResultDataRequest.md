# UpsertStructuredResultDataRequest

The details of the structured unit result data item to upsert into Lusid.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | 
**data** | [**StructuredResultData**](StructuredResultData.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_structured_result_data_request import UpsertStructuredResultDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertStructuredResultDataRequest from a JSON string
upsert_structured_result_data_request_instance = UpsertStructuredResultDataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertStructuredResultDataRequest.to_json()

# convert the object into a dict
upsert_structured_result_data_request_dict = upsert_structured_result_data_request_instance.to_dict()
# create an instance of UpsertStructuredResultDataRequest from a dict
upsert_structured_result_data_request_form_dict = upsert_structured_result_data_request.from_dict(upsert_structured_result_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


