# ConfigurationRecipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User given string name (code) to identify the recipe. | 
**market** | [**MarketContext**](MarketContext.md) |  | [optional] 
**pricing** | [**PricingContext**](PricingContext.md) |  | [optional] 
**aggregation** | [**AggregationContext**](AggregationContext.md) |  | [optional] 
**inherited_recipes** | [**list[ResourceId]**](ResourceId.md) | A list of parent recipes (scope,code) that can be used to share functionality between recipes. For instance one might use common recipes to set up  pricing for individual asset classes, e.g. rates or credit, and then combine them into a single recipe to be used by an exotics desk in conjunction with  some overrides that it requires for models or other pricing options. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


