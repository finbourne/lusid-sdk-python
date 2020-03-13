# StructuredMarketDataId

An identifier that uniquely describes an item of structured market data such as an interest rate curve or volatility surface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the structured market data, e.g. &#39;DataScope&#39;, &#39;LUSID&#39;, &#39;ISDA&#39; etc. | 
**price_source** | **str** | The source or originator of the structured market data, e.g. a bank or financial institution. | [optional] 
**lineage** | **str** | Description of the structured market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of structured market data is/was updated/inserted with. | [optional] 
**market_element_type** | **str** | The type of the market element that the market entity represents, e.g. a vol surface or credit curve | [optional] 
**market_asset** | **str** | The name of the market entity that the document represents | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


