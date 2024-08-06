# RecipeComposer

Recipe composer is an object used to dynamically compose Configuration Recipe from atomic operations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used when updating or inserting the Recipe Composer. | 
**code** | **str** | User given string name (code) to identify the recipe. | 
**operations** | [**List[RecipeBlock]**](RecipeBlock.md) | Atomic operations used to compose a Configuration Recipe. | [optional] 

## Example

```python
from lusid.models.recipe_composer import RecipeComposer

# TODO update the JSON string below
json = "{}"
# create an instance of RecipeComposer from a JSON string
recipe_composer_instance = RecipeComposer.from_json(json)
# print the JSON string representation of the object
print RecipeComposer.to_json()

# convert the object into a dict
recipe_composer_dict = recipe_composer_instance.to_dict()
# create an instance of RecipeComposer from a dict
recipe_composer_form_dict = recipe_composer.from_dict(recipe_composer_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


