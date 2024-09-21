# UpdateReferenceDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_definitions** | [**List[FieldDefinition]**](FieldDefinition.md) | Definition of a reference data field. | 
**request_values** | [**List[FieldValue]**](FieldValue.md) | Reference data. | 

## Example

```python
from lusid.models.update_reference_data_request import UpdateReferenceDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReferenceDataRequest from a JSON string
update_reference_data_request_instance = UpdateReferenceDataRequest.from_json(json)
# print the JSON string representation of the object
print UpdateReferenceDataRequest.to_json()

# convert the object into a dict
update_reference_data_request_dict = update_reference_data_request_instance.to_dict()
# create an instance of UpdateReferenceDataRequest from a dict
update_reference_data_request_form_dict = update_reference_data_request.from_dict(update_reference_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


