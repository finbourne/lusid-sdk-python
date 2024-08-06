# UpsertResultValuesDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | 
**key** | **Dict[str, str]** | The structured unit result data key. | [optional] 
**data_address** | **str** | The address of the piece of unit result data | [optional] 
**result_value** | [**ResultValue**](ResultValue.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_result_values_data_request import UpsertResultValuesDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertResultValuesDataRequest from a JSON string
upsert_result_values_data_request_instance = UpsertResultValuesDataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertResultValuesDataRequest.to_json()

# convert the object into a dict
upsert_result_values_data_request_dict = upsert_result_values_data_request_instance.to_dict()
# create an instance of UpsertResultValuesDataRequest from a dict
upsert_result_values_data_request_form_dict = upsert_result_values_data_request.from_dict(upsert_result_values_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


