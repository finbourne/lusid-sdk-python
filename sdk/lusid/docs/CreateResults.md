# CreateResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective market date for which results are calculated and are to be stored. | 
**entity_scope** | **str** | Scope of the entity code | 
**entity_code** | **str** | The code of the entity for which the data has been calculated. | 
**calculation_scope** | **str** | Scope of the calculation code. | 
**calculation_code** | **str** | This is the identifier which denotes some hash of, or recipe, that cumulatively represents the configuration through which  the results being stored are obtained. For example, the recipe denotes the pricing model, the market data and any other  settings. If the results were calculated externally it should be some repeatable hash or other Id that denotes the particular  configuration under which those results were obtained. | 
**format** | **str** | The format in which the results are stored/structured. | [optional] 
**data** | **str** | The data that should be stored in the results cube. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


