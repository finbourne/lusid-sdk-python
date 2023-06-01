# PortfolioDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**origin_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) |  | 
**base_currency** | **str** | The base currency of the transaction portfolio. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**sub_holding_keys** | **list[str]** |  | [optional] 
**instrument_scopes** | **list[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio. | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**amortisation_method** | **str** | The amortisation method the portfolio is using in the calculation. This can be &#39;NoAmortisation&#39;, &#39;StraightLine&#39; or &#39;EffectiveYield&#39;. | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


