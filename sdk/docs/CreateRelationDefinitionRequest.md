# CreateRelationDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relation exists in. | 
**code** | **str** | The code of the relation. Together with the scope this uniquely defines the relation. | 
**source_entity_domain** | **str** | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**target_entity_domain** | **str** | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**display_name** | **str** | The display name of the relation. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 

## Example

```python
from lusid.models.create_relation_definition_request import CreateRelationDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRelationDefinitionRequest from a JSON string
create_relation_definition_request_instance = CreateRelationDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateRelationDefinitionRequest.to_json()

# convert the object into a dict
create_relation_definition_request_dict = create_relation_definition_request_instance.to_dict()
# create an instance of CreateRelationDefinitionRequest from a dict
create_relation_definition_request_form_dict = create_relation_definition_request.from_dict(create_relation_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


