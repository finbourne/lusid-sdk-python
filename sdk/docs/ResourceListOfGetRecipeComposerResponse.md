# ResourceListOfGetRecipeComposerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[GetRecipeComposerResponse]**](GetRecipeComposerResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_get_recipe_composer_response import ResourceListOfGetRecipeComposerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfGetRecipeComposerResponse from a JSON string
resource_list_of_get_recipe_composer_response_instance = ResourceListOfGetRecipeComposerResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfGetRecipeComposerResponse.to_json()

# convert the object into a dict
resource_list_of_get_recipe_composer_response_dict = resource_list_of_get_recipe_composer_response_instance.to_dict()
# create an instance of ResourceListOfGetRecipeComposerResponse from a dict
resource_list_of_get_recipe_composer_response_form_dict = resource_list_of_get_recipe_composer_response.from_dict(resource_list_of_get_recipe_composer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


