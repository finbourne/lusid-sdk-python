# Relation

Representation of a Relation between a requested entity with the stated entity as RelationedEntityId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**related_entity_id** | **Dict[str, str]** |  | 
**traversal_direction** | **str** |  | 
**traversal_description** | **str** |  | 
**effective_from** | **datetime** |  | [optional] 

## Example

```python
from lusid.models.relation import Relation

# TODO update the JSON string below
json = "{}"
# create an instance of Relation from a JSON string
relation_instance = Relation.from_json(json)
# print the JSON string representation of the object
print Relation.to_json()

# convert the object into a dict
relation_dict = relation_instance.to_dict()
# create an instance of Relation from a dict
relation_form_dict = relation.from_dict(relation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


