# TransactionConfigurationTypeAlias


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transaction_class** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transaction_group** | **str** | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead | [optional] 
**source** | **str** | Used to group a set of transaction types | [optional] 
**transaction_roles** | **str** | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles | 
**is_default** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


