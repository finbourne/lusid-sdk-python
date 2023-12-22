# CustomEntityDefinition

Representation of Custom Entity Definition on LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type_name** | **str** | The name provided when the custom entity type was created. This has been prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. | 
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | [optional] 
**entity_type** | **str** | The identifier for the custom entity type, derived from the “entityTypeName” provided on creation. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 
**version** | [**Version**](Version.md) |  | 

## Example

```python
from lusid.models.custom_entity_definition import CustomEntityDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityDefinition from a JSON string
custom_entity_definition_instance = CustomEntityDefinition.from_json(json)
# print the JSON string representation of the object
print CustomEntityDefinition.to_json()

# convert the object into a dict
custom_entity_definition_dict = custom_entity_definition_instance.to_dict()
# create an instance of CustomEntityDefinition from a dict
custom_entity_definition_form_dict = custom_entity_definition.from_dict(custom_entity_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


