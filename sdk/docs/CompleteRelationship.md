# CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**target_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**outward_description** | **str** | Description of the relationship based on relationship definition&#39;s outward description. | 
**inward_description** | **str** | Description of the relationship based on relationship definition&#39;s inward description. | 
**effective_from** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime to which the relationship is valid until. | [optional] 

## Example

```python
from lusid.models.complete_relationship import CompleteRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteRelationship from a JSON string
complete_relationship_instance = CompleteRelationship.from_json(json)
# print the JSON string representation of the object
print CompleteRelationship.to_json()

# convert the object into a dict
complete_relationship_dict = complete_relationship_instance.to_dict()
# create an instance of CompleteRelationship from a dict
complete_relationship_form_dict = complete_relationship.from_dict(complete_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


