# AccountedTransaction

The Valuation Point Data Response for the Fund and specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_date** | **datetime** | The transaction&#39;s accounting date. | [optional] 
**journal_entry_action** | **str** | The journal entry line action associated with this transaction. | [optional] 
**transaction** | [**OutputTransaction**](OutputTransaction.md) |  | [optional] 
**portfolio_id** | [**PortfolioId**](PortfolioId.md) |  | [optional] 

## Example

```python
from lusid.models.accounted_transaction import AccountedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AccountedTransaction from a JSON string
accounted_transaction_instance = AccountedTransaction.from_json(json)
# print the JSON string representation of the object
print AccountedTransaction.to_json()

# convert the object into a dict
accounted_transaction_dict = accounted_transaction_instance.to_dict()
# create an instance of AccountedTransaction from a dict
accounted_transaction_form_dict = accounted_transaction.from_dict(accounted_transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


