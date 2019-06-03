# OutputTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique transaction identifier | [optional] 
**type** | **str** | LUSID transaction type code - Buy, Sell, StockIn, StockOut, etc | [optional] 
**description** | **str** | LUSID transaction description | [optional] 
**instrument_identifiers** | **dict(str, str)** | Unique instrument identifiers | [optional] 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | [optional] 
**transaction_date** | **datetime** | Transaction date | [optional] 
**settlement_date** | **datetime** | Settlement date | [optional] 
**units** | **float** | Quantity of trade in units of the instrument | [optional] 
**transaction_amount** | **float** | Total value of the transaction in trade currency | [optional] 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**exchange_rate** | **float** | Rate between transaction and settlement currency | [optional] 
**transaction_to_portfolio_rate** | **float** | Rate between transaction and portfolio currency | [optional] 
**transaction_currency** | **str** | Transaction currency | [optional] 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**counterparty_id** | **str** | Counterparty identifier | [optional] 
**source** | **str** | Where this transaction came from | [optional] 
**netting_set** | **str** |  | [optional] 
**transaction_status** | **str** | Transaction status (active, amended or cancelled) | [optional] 
**entry_date_time** | **datetime** | Date / time the transaction was booked into LUSID | [optional] 
**cancel_date_time** | **datetime** | Date / time the cancellation was booked into LUSID | [optional] 
**realised_gain_loss** | [**list[RealisedGainLoss]**](RealisedGainLoss.md) | Collection of gains or losses | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


