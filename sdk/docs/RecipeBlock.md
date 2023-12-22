# RecipeBlock

An atomic operation used in Recipe composer to compose a Configuration Recipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**RecipeValue**](RecipeValue.md) |  | [optional] 
**path** | **str** | Path of the Value that the operation is to be performed on. | [optional] 
**op** | **str** | Operation to be performed on the part of the value. | [optional] 

## Example

```python
from lusid.models.recipe_block import RecipeBlock

# TODO update the JSON string below
json = "{}"
# create an instance of RecipeBlock from a JSON string
recipe_block_instance = RecipeBlock.from_json(json)
# print the JSON string representation of the object
print RecipeBlock.to_json()

# convert the object into a dict
recipe_block_dict = recipe_block_instance.to_dict()
# create an instance of RecipeBlock from a dict
recipe_block_form_dict = recipe_block.from_dict(recipe_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


