# Transaction

A list of transactions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | [optional] 
**instrument_scope** | **str** | The scope in which the transaction&#39;s instrument lies. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**transaction_date** | **datetime** | The date of the transaction. | 
**settlement_date** | **datetime** | The settlement date of the transaction. | 
**units** | **float** | The number of units transacted in the associated instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**entry_date_time** | **datetime** | The asAt datetime that the transaction was added to LUSID. | [optional] 
**otc_confirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 
**transaction_status** | **str** | The status of the transaction. The available values are: Active, Amended, Cancelled | [optional] 
**cancel_date_time** | **datetime** | If the transaction has been cancelled, the asAt datetime that the transaction was cancelled. | [optional] 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account** | [**CustodianAccount**](CustodianAccount.md) |  | [optional] 

## Example

```python
from lusid.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print Transaction.to_json()

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


