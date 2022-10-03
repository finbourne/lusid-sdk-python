# Portfolio

A list of portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | 
**display_name** | **str** | The name of the portfolio. | 
**description** | **str** | The long form description of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] 
**base_currency** | **str** | The base currency of the portfolio. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**instrument_scopes** | **list[str]** | The instrument scope resolution strategy of this portfolio. | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**amortisation_method** | **str** | The amortisation method the portfolio is using in the calculation. This can be &#39;NoAmortisation&#39;, &#39;StraightLine&#39; or &#39;EffectiveYield&#39;. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


