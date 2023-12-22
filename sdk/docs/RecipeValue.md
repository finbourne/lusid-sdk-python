# RecipeValue

Recipe value represents a data that is then used to perform an atomic operation which is then used in composition of Configuration Recipe.  This object either includes the data itself (in json form or as simple string) or is a reference where the data can be obtained from (from a Configuration Recipe say).  Only one field is to be populated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_json** | **str** | Field to allow providing a potentially complex json value. | [optional] 
**as_string** | **str** | For simple value, a single input value, note complex nested objects are not allowed here. | [optional] 
**from_recipe** | [**FromRecipe**](FromRecipe.md) |  | [optional] 

## Example

```python
from lusid.models.recipe_value import RecipeValue

# TODO update the JSON string below
json = "{}"
# create an instance of RecipeValue from a JSON string
recipe_value_instance = RecipeValue.from_json(json)
# print the JSON string representation of the object
print RecipeValue.to_json()

# convert the object into a dict
recipe_value_dict = recipe_value_instance.to_dict()
# create an instance of RecipeValue from a dict
recipe_value_form_dict = recipe_value.from_dict(recipe_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


