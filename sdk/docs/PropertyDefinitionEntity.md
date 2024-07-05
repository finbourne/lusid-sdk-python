# PropertyDefinitionEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_unique_id** | **str** | The unique id of the entity. | 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**status** | **str** | The status of the entity at the current time. | 
**as_at_deleted** | **datetime** | The asAt datetime at which the entity was deleted. | [optional] 
**user_id_deleted** | **str** | The unique id of the user who deleted the entity. | [optional] 
**request_id_deleted** | **str** | The unique request id of the command that deleted the entity. | [optional] 
**effective_at_created** | **datetime** | The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt. | [optional] 
**prevailing_property_definition** | [**PropertyDefinition**](PropertyDefinition.md) |  | [optional] 
**deleted_property_definition** | [**PropertyDefinition**](PropertyDefinition.md) |  | [optional] 
**previewed_status** | **str** | The status of the previewed entity. | [optional] 
**previewed_property_definition** | [**PropertyDefinition**](PropertyDefinition.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.property_definition_entity import PropertyDefinitionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDefinitionEntity from a JSON string
property_definition_entity_instance = PropertyDefinitionEntity.from_json(json)
# print the JSON string representation of the object
print PropertyDefinitionEntity.to_json()

# convert the object into a dict
property_definition_entity_dict = property_definition_entity_instance.to_dict()
# create an instance of PropertyDefinitionEntity from a dict
property_definition_entity_form_dict = property_definition_entity.from_dict(property_definition_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


