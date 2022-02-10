# CreateReferencePortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the reference portfolio. | 
**description** | **str** | A long form text description of the portfolio. | [optional] 
**code** | **str** | Unique identifier for the portfolio. | 
**created** | **datetime** | The original creation date, defaults to today if not specified when creating a portfolio. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Portfolio properties to add to the portfolio. | [optional] 
**instrument_scopes** | **list[str]** | Instrument Scopes. | [optional] 
**base_currency** | **str** | The base currency of the transaction portfolio in ISO 4217 currency code format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


