# FromRecipe


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from lusid.models.from_recipe import FromRecipe

# TODO update the JSON string below
json = "{}"
# create an instance of FromRecipe from a JSON string
from_recipe_instance = FromRecipe.from_json(json)
# print the JSON string representation of the object
print FromRecipe.to_json()

# convert the object into a dict
from_recipe_dict = from_recipe_instance.to_dict()
# create an instance of FromRecipe from a dict
from_recipe_form_dict = from_recipe.from_dict(from_recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


