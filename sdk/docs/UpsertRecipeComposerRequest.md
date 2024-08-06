# UpsertRecipeComposerRequest

A recipe composer that is to be stored in the recipe composer data store or used for inline resolving.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_composer** | [**RecipeComposer**](RecipeComposer.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_recipe_composer_request import UpsertRecipeComposerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRecipeComposerRequest from a JSON string
upsert_recipe_composer_request_instance = UpsertRecipeComposerRequest.from_json(json)
# print the JSON string representation of the object
print UpsertRecipeComposerRequest.to_json()

# convert the object into a dict
upsert_recipe_composer_request_dict = upsert_recipe_composer_request_instance.to_dict()
# create an instance of UpsertRecipeComposerRequest from a dict
upsert_recipe_composer_request_form_dict = upsert_recipe_composer_request.from_dict(upsert_recipe_composer_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


