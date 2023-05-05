# CreateTransactionPortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the transaction portfolio. | 
**description** | **str** | A description for the transaction portfolio. | [optional] 
**code** | **str** | The code of the transaction portfolio. Together with the scope this uniquely identifies the transaction portfolio. | 
**created** | **datetime** | The effective datetime at which to create the transaction portfolio. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] 
**base_currency** | **str** | The base currency of the transaction portfolio in ISO 4217 currency code format. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**sub_holding_keys** | **list[str]** | A set of unique transaction properties to group the transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#39;Portfolio&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Note these properties must be pre-defined. | [optional] 
**instrument_scopes** | **list[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio. | [optional] 
**amortisation_method** | **str** | The amortisation method the portfolio is using in the calculation. This can be &#39;NoAmortisation&#39;, &#39;StraightLine&#39; or &#39;EffectiveYield&#39;. | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


