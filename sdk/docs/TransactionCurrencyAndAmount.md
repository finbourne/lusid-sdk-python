# TransactionCurrencyAndAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 

## Example

```python
from lusid.models.transaction_currency_and_amount import TransactionCurrencyAndAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCurrencyAndAmount from a JSON string
transaction_currency_and_amount_instance = TransactionCurrencyAndAmount.from_json(json)
# print the JSON string representation of the object
print TransactionCurrencyAndAmount.to_json()

# convert the object into a dict
transaction_currency_and_amount_dict = transaction_currency_and_amount_instance.to_dict()
# create an instance of TransactionCurrencyAndAmount from a dict
transaction_currency_and_amount_form_dict = transaction_currency_and_amount.from_dict(transaction_currency_and_amount_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


