# CreateCustomEntityTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | **str** | A name for the custom entity type. This will be prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. | 
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 

## Example

```python
from lusid.models.create_custom_entity_type_request import CreateCustomEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomEntityTypeRequest from a JSON string
create_custom_entity_type_request_instance = CreateCustomEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print CreateCustomEntityTypeRequest.to_json()

# convert the object into a dict
create_custom_entity_type_request_dict = create_custom_entity_type_request_instance.to_dict()
# create an instance of CreateCustomEntityTypeRequest from a dict
create_custom_entity_type_request_form_dict = create_custom_entity_type_request.from_dict(create_custom_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


