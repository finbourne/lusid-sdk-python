# PortfolioSearchResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**base_currency** | **str** | The base currency of the portfolio. This will be an empty string for reference portfolios. | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


