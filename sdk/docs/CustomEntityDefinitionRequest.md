# CustomEntityDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | **str** | A name for the custom entity type. This will be prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. | 
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 

## Example

```python
from lusid.models.custom_entity_definition_request import CustomEntityDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityDefinitionRequest from a JSON string
custom_entity_definition_request_instance = CustomEntityDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CustomEntityDefinitionRequest.to_json()

# convert the object into a dict
custom_entity_definition_request_dict = custom_entity_definition_request_instance.to_dict()
# create an instance of CustomEntityDefinitionRequest from a dict
custom_entity_definition_request_form_dict = custom_entity_definition_request.from_dict(custom_entity_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


