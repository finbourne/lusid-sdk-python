# CustomEntityEntity


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
**prevailing_custom_entity** | [**CustomEntityResponse**](CustomEntityResponse.md) |  | [optional] 
**deleted_custom_entity** | [**CustomEntityResponse**](CustomEntityResponse.md) |  | [optional] 
**previewed_status** | **str** | The status of the previewed entity. | [optional] 
**previewed_custom_entity** | [**CustomEntityResponse**](CustomEntityResponse.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.custom_entity_entity import CustomEntityEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityEntity from a JSON string
custom_entity_entity_instance = CustomEntityEntity.from_json(json)
# print the JSON string representation of the object
print CustomEntityEntity.to_json()

# convert the object into a dict
custom_entity_entity_dict = custom_entity_entity_instance.to_dict()
# create an instance of CustomEntityEntity from a dict
custom_entity_entity_form_dict = custom_entity_entity.from_dict(custom_entity_entity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


