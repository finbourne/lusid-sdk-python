# StructuredResultDataId

An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The platform or vendor that provided the structured result data, e.g. &#39;client&#39;. This is primarily of interest when data could have been sourced from multiple sources | 
**code** | **str** | The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of structured market data is/was updated/inserted with. | [optional] 
**result_type** | **str** | An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#39;risk result&#39;, &#39;cashflow&#39;, &#39;index&#39; or similar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


