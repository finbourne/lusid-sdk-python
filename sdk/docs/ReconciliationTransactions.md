# ReconciliationTransactions

Specification for the transactions of a scheduled reconciliation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_window** | [**DateRange**](DateRange.md) |  | [optional] 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.reconciliation_transactions import ReconciliationTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationTransactions from a JSON string
reconciliation_transactions_instance = ReconciliationTransactions.from_json(json)
# print the JSON string representation of the object
print ReconciliationTransactions.to_json()

# convert the object into a dict
reconciliation_transactions_dict = reconciliation_transactions_instance.to_dict()
# create an instance of ReconciliationTransactions from a dict
reconciliation_transactions_form_dict = reconciliation_transactions.from_dict(reconciliation_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


