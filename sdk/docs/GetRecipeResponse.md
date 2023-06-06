# GetRecipeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_recipe_response import GetRecipeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecipeResponse from a JSON string
get_recipe_response_instance = GetRecipeResponse.from_json(json)
# print the JSON string representation of the object
print GetRecipeResponse.to_json()

# convert the object into a dict
get_recipe_response_dict = get_recipe_response_instance.to_dict()
# create an instance of GetRecipeResponse from a dict
get_recipe_response_form_dict = get_recipe_response.from_dict(get_recipe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


