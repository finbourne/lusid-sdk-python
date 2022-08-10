# CreateDerivedTransactionPortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the derived transaction portfolio. | 
**description** | **str** | A description for the derived transaction portfolio. | [optional] 
**code** | **str** | The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**created** | **datetime** | This will be auto-populated to be the parent portfolio creation date. | [optional] 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | Determines the accounting treatment given to the transaction portfolio&#39;s tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**sub_holding_keys** | **list[str]** | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**instrument_scopes** | **list[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


