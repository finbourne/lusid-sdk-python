# ExecutionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | The unique identifier of the Execution Report (8) message as assigned by sell-side. FIX field 17. | 
**side** | **str** | The side of the order. FIX field 54. | 
**instrument_identifiers** | **dict(str, str)** | A set of instrument identifiers that can resolve the execution to a unique instrument. | 
**transaction_time** | **datetime** | Time of execution/order creation. FIX field 60. | 
**last_shares** | **float** | Quantity (e.g. shares) bought/sold on this (last) fill. FIX field 32. | 
**last_px** | **float** | Price of this (last) fill. FIX field 31. | 
**currency** | **str** | The currency used for the price. FIX field 15. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


