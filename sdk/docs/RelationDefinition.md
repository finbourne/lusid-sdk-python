# RelationDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source_entity_domain** | **str** | The entity domain of the source entity object. | [optional] 
**target_entity_domain** | **str** | The entity domain of the target entity object. | [optional] 
**display_name** | **str** | The display name of the relation. | [optional] 
**outward_description** | **str** | The description to relate source entity object and target entity object | [optional] 
**inward_description** | **str** | The description to relate target entity object and source entity object | [optional] 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.relation_definition import RelationDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RelationDefinition from a JSON string
relation_definition_instance = RelationDefinition.from_json(json)
# print the JSON string representation of the object
print RelationDefinition.to_json()

# convert the object into a dict
relation_definition_dict = relation_definition_instance.to_dict()
# create an instance of RelationDefinition from a dict
relation_definition_form_dict = relation_definition.from_dict(relation_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


