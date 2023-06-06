# CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_creation_market_data_scopes** | **List[str]** | The scopes in which the recipe creation would look for quotes/data. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**inline_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**as_at** | **datetime** | The asAt date to use | [optional] 
**effective_at** | **str** | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. | 

## Example

```python
from lusid.models.create_recipe_request import CreateRecipeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipeRequest from a JSON string
create_recipe_request_instance = CreateRecipeRequest.from_json(json)
# print the JSON string representation of the object
print CreateRecipeRequest.to_json()

# convert the object into a dict
create_recipe_request_dict = create_recipe_request_instance.to_dict()
# create an instance of CreateRecipeRequest from a dict
create_recipe_request_form_dict = create_recipe_request.from_dict(create_recipe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


