# ExecutionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | FIX Field 17.  Unique execution identifier. | 
**side** | **str** | FIX Field 54. | 
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers. | 
**transaction_time** | **datetime** | FIX field 60.  Time the transaction represented by this ExecutionReport occurred. | 
**last_shares** | **float** | FIX field 32. | 
**last_px** | **float** | FIX field 31. | 
**currency** | **str** | FIX field 15. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


