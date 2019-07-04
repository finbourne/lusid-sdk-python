# TransactionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. If it hasn&#39;t been pre-configured the transaction will still be upserted however you will be unable to generate the resultant holdings for the portfolio that contains this transaction as LUSID does not know how to process it. | 
**instrument_identifiers** | **dict(str, str)** | A set of instrument identifiers to use to resolve the transaction to a unique instrument. | 
**transaction_date** | **str** | The date of the transaction. | 
**settlement_date** | **str** | The settlement date of the transaction. | 
**units** | **float** | The number of units transacted in the associated instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency. For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md) | Set of unique transaction properties and associated values to store with the transaction. Each property must be from the &#39;Trade&#39; domain. | [optional] 
**counterparty_id** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


