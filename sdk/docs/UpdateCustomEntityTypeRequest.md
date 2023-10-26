# UpdateCustomEntityTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 

## Example

```python
from lusid.models.update_custom_entity_type_request import UpdateCustomEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomEntityTypeRequest from a JSON string
update_custom_entity_type_request_instance = UpdateCustomEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCustomEntityTypeRequest.to_json()

# convert the object into a dict
update_custom_entity_type_request_dict = update_custom_entity_type_request_instance.to_dict()
# create an instance of UpdateCustomEntityTypeRequest from a dict
update_custom_entity_type_request_form_dict = update_custom_entity_type_request.from_dict(update_custom_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


