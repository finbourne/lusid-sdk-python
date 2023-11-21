# UpsertRecipeRequest

A recipe or recipe snippet that is to be stored in the recipe structured data store.  Only one of these must be present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_recipe_request import UpsertRecipeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRecipeRequest from a JSON string
upsert_recipe_request_instance = UpsertRecipeRequest.from_json(json)
# print the JSON string representation of the object
print UpsertRecipeRequest.to_json()

# convert the object into a dict
upsert_recipe_request_dict = upsert_recipe_request_instance.to_dict()
# create an instance of UpsertRecipeRequest from a dict
upsert_recipe_request_form_dict = upsert_recipe_request.from_dict(upsert_recipe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


