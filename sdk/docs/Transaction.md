# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique transaction identifier | 
**type** | **str** | LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | 
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers | [optional] 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**transaction_date** | **datetime** | Transaction date | 
**settlement_date** | **datetime** | Settlement date | 
**units** | **float** | Quantity of trade in units of the instrument | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | Rate between transaction and settlement currency | [optional] 
**transaction_currency** | **str** | Transaction currency | [optional] 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**counterparty_id** | **str** | Counterparty identifier | [optional] 
**source** | **str** | Where this transaction came from | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


