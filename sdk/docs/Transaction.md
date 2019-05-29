# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique transaction identifier | 
**type** | **str** | LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | 
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers. | [optional] 
**instrument_uid** | **str** | Unique instrument identifier | 
**transaction_date** | **datetime** | Transaction date | 
**settlement_date** | **datetime** | Settlement date | 
**units** | **float** | Quantity of transaction in units of the instrument | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | Rate between transaction and settle currency | [optional] 
**transaction_currency** | **str** | Transaction currency | [optional] 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**counterparty_id** | **str** | Counterparty identifier | [optional] 
**source** | **str** | Where this transaction came from | 
**netting_set** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


