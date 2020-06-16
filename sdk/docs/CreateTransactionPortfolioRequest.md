# CreateTransactionPortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the transaction portfolio. | 
**description** | **str** | A long form description of the transaction portfolio. | [optional] 
**code** | **str** | The code that the transaction portfolio will be created with. Together with the scope this uniquely identifies the transaction portfolio. | 
**created** | **datetime** | The effective datetime at which the transaction portfolio will be created. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] 
**base_currency** | **str** | The base currency of the transaction portfolio. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | Determines the accounting treatment given to the transaction portfolio&#39;s tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**sub_holding_keys** | **list[str]** | A set of unique transaction properties to group the transaction portfolio&#39;s holdings by. Each property must be from the &#39;Transaction&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;Transaction/strategies/quantsignal&#39;. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of unique portfolio properties to add to the transaction portfolio. Each property must be from the &#39;Portfolio&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. These properties must be pre-defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


