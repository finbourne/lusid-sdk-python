# PagedResourceListOfCustomEntityDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CustomEntityDefinition]**](CustomEntityDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_custom_entity_definition import PagedResourceListOfCustomEntityDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCustomEntityDefinition from a JSON string
paged_resource_list_of_custom_entity_definition_instance = PagedResourceListOfCustomEntityDefinition.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCustomEntityDefinition.to_json()

# convert the object into a dict
paged_resource_list_of_custom_entity_definition_dict = paged_resource_list_of_custom_entity_definition_instance.to_dict()
# create an instance of PagedResourceListOfCustomEntityDefinition from a dict
paged_resource_list_of_custom_entity_definition_form_dict = paged_resource_list_of_custom_entity_definition.from_dict(paged_resource_list_of_custom_entity_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


