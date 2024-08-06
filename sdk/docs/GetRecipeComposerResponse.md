# GetRecipeComposerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**RecipeComposer**](RecipeComposer.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_recipe_composer_response import GetRecipeComposerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecipeComposerResponse from a JSON string
get_recipe_composer_response_instance = GetRecipeComposerResponse.from_json(json)
# print the JSON string representation of the object
print GetRecipeComposerResponse.to_json()

# convert the object into a dict
get_recipe_composer_response_dict = get_recipe_composer_response_instance.to_dict()
# create an instance of GetRecipeComposerResponse from a dict
get_recipe_composer_response_form_dict = get_recipe_composer_response.from_dict(get_recipe_composer_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


