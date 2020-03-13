# Transaction

A list of transactions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**instrument_identifiers** | **dict(str, str)** | The set of instrument identifiers that can be used to resolve the transaction to a unique instrument. | [optional] 
**instrument_uid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**transaction_date** | **datetime** | The date of the transaction. | 
**settlement_date** | **datetime** | The settlement date of the transaction. | 
**units** | **float** | The number of units transacted in the associated instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency. For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


