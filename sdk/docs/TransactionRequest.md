# TransactionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique transaction identifier | 
**type** | **str** | LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | 
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers | 
**transaction_date** | **str** | Transaction date | 
**settlement_date** | **str** | Settlement date | 
**units** | **float** | Quantity of trade in units of the instrument | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | Rate between transaction and settlement currency | [optional] 
**transaction_currency** | **str** | Transaction currency | [optional] 
**properties** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md) |  | [optional] 
**counterparty_id** | **str** | Counterparty identifier | [optional] 
**source** | **str** | Where this transaction came from | [optional] 
**netting_set** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


