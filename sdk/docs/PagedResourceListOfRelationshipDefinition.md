# PagedResourceListOfRelationshipDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[RelationshipDefinition]**](RelationshipDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_relationship_definition import PagedResourceListOfRelationshipDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfRelationshipDefinition from a JSON string
paged_resource_list_of_relationship_definition_instance = PagedResourceListOfRelationshipDefinition.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfRelationshipDefinition.to_json()

# convert the object into a dict
paged_resource_list_of_relationship_definition_dict = paged_resource_list_of_relationship_definition_instance.to_dict()
# create an instance of PagedResourceListOfRelationshipDefinition from a dict
paged_resource_list_of_relationship_definition_form_dict = paged_resource_list_of_relationship_definition.from_dict(paged_resource_list_of_relationship_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


