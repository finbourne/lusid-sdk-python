# PortfolioSearchResult

A list of portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. | [readonly] 
**href** | **str** | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] [readonly] 
**description** | **str** | The long form description of the portfolio. | [optional] [readonly] 
**display_name** | **str** | The name of the portfolio. | [readonly] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [readonly] 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**base_currency** | **str** | The base currency of the portfolio. This will be an empty string for reference portfolios. | [optional] [readonly] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] [readonly] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


