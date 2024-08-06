# CompleteRelation

Representation of a relation containing details of source and target entities, and both outward and inward descriptions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity_id** | **Dict[str, str]** |  | 
**target_entity_id** | **Dict[str, str]** |  | 
**outward_description** | **str** |  | 
**inward_description** | **str** |  | 
**effective_from** | **datetime** |  | [optional] 

## Example

```python
from lusid.models.complete_relation import CompleteRelation

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteRelation from a JSON string
complete_relation_instance = CompleteRelation.from_json(json)
# print the JSON string representation of the object
print CompleteRelation.to_json()

# convert the object into a dict
complete_relation_dict = complete_relation_instance.to_dict()
# create an instance of CompleteRelation from a dict
complete_relation_form_dict = complete_relation.from_dict(complete_relation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


