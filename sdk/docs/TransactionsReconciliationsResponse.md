# TransactionsReconciliationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**Mapping**](Mapping.md) |  | [optional] 
**data** | [**List[ReconciledTransaction]**](ReconciledTransaction.md) | The result of this reconciliation | [optional] 

## Example

```python
from lusid.models.transactions_reconciliations_response import TransactionsReconciliationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsReconciliationsResponse from a JSON string
transactions_reconciliations_response_instance = TransactionsReconciliationsResponse.from_json(json)
# print the JSON string representation of the object
print TransactionsReconciliationsResponse.to_json()

# convert the object into a dict
transactions_reconciliations_response_dict = transactions_reconciliations_response_instance.to_dict()
# create an instance of TransactionsReconciliationsResponse from a dict
transactions_reconciliations_response_form_dict = transactions_reconciliations_response.from_dict(transactions_reconciliations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


