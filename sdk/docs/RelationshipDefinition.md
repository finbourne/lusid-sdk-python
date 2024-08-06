# RelationshipDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity_type** | **str** | The entity type of the source entity object. | 
**target_entity_type** | **str** | The entity type of the target entity object. | 
**display_name** | **str** | The display name of the relationship. | 
**outward_description** | **str** | The description to relate source entity object and target entity object | 
**inward_description** | **str** | The description to relate target entity object and source entity object | 
**life_time** | **str** | Describes how the relationships can change over time. | 
**relationship_cardinality** | **str** | Describes the cardinality of the relationship between source entity and target entity. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.relationship_definition import RelationshipDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipDefinition from a JSON string
relationship_definition_instance = RelationshipDefinition.from_json(json)
# print the JSON string representation of the object
print RelationshipDefinition.to_json()

# convert the object into a dict
relationship_definition_dict = relationship_definition_instance.to_dict()
# create an instance of RelationshipDefinition from a dict
relationship_definition_form_dict = relationship_definition.from_dict(relationship_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


