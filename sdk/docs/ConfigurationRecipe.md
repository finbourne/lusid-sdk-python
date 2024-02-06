# ConfigurationRecipe

The Configuration or Calculation Recipe controls how LUSID processes a given request.  This can be used to change where market data used in pricing is loaded from and in what order, or which model is used to  price a given instrument as well as how aggregation will process the produced results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used when updating or inserting the Configuration Recipe. | 
**code** | **str** | User given string name (code) to identify the recipe. | 
**market** | [**MarketContext**](MarketContext.md) |  | [optional] 
**pricing** | [**PricingContext**](PricingContext.md) |  | [optional] 
**aggregation** | [**AggregationContext**](AggregationContext.md) |  | [optional] 
**description** | **str** | User can assign a description to understand more humanly the recipe. | [optional] 
**holding** | [**HoldingContext**](HoldingContext.md) |  | [optional] 
**translation** | [**TranslationContext**](TranslationContext.md) |  | [optional] 

## Example

```python
from lusid.models.configuration_recipe import ConfigurationRecipe

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationRecipe from a JSON string
configuration_recipe_instance = ConfigurationRecipe.from_json(json)
# print the JSON string representation of the object
print ConfigurationRecipe.to_json()

# convert the object into a dict
configuration_recipe_dict = configuration_recipe_instance.to_dict()
# create an instance of ConfigurationRecipe from a dict
configuration_recipe_form_dict = configuration_recipe.from_dict(configuration_recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


