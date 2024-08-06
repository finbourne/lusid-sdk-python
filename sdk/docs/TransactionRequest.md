# TransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction. | 
**type** | **str** | The type of the transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. | 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 
**transaction_date** | **str** | The date of the transaction. | 
**settlement_date** | **str** | The settlement date of the transaction. | 
**units** | **float** | The number of units of the transacted instrument. | 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchange_rate** | **float** | The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate. | [optional] 
**transaction_currency** | **str** | The transaction currency. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**counterparty_id** | **str** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**otc_confirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print TransactionRequest.to_json()

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_form_dict = transaction_request.from_dict(transaction_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


