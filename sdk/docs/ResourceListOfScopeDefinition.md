# ResourceListOfScopeDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ScopeDefinition]**](ScopeDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_scope_definition import ResourceListOfScopeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfScopeDefinition from a JSON string
resource_list_of_scope_definition_instance = ResourceListOfScopeDefinition.from_json(json)
# print the JSON string representation of the object
print ResourceListOfScopeDefinition.to_json()

# convert the object into a dict
resource_list_of_scope_definition_dict = resource_list_of_scope_definition_instance.to_dict()
# create an instance of ResourceListOfScopeDefinition from a dict
resource_list_of_scope_definition_form_dict = resource_list_of_scope_definition.from_dict(resource_list_of_scope_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


