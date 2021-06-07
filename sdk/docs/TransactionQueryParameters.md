# TransactionQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. | 
**end_date** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. | 
**query_mode** | **str** | The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#39;TradeDate&#39; if not specified. The available values are: TradeDate, SettleDate | [optional] 
**show_cancelled_transactions** | **bool** | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


