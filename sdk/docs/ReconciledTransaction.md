# ReconciledTransaction

Information about reconciled transactions.  At least one of Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Left and Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Right will be populated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**Transaction**](Transaction.md) |  | [optional] 
**right** | [**Transaction**](Transaction.md) |  | [optional] 
**percentage_match** | **float** | How good a match this is considered to be. | [optional] 
**mapping_rule_set_results** | **List[bool]** | The result of each individual mapping rule result.  Will only be present if both Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Left and Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Right are populated. | [optional] 

## Example

```python
from lusid.models.reconciled_transaction import ReconciledTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciledTransaction from a JSON string
reconciled_transaction_instance = ReconciledTransaction.from_json(json)
# print the JSON string representation of the object
print ReconciledTransaction.to_json()

# convert the object into a dict
reconciled_transaction_dict = reconciled_transaction_instance.to_dict()
# create an instance of ReconciledTransaction from a dict
reconciled_transaction_form_dict = reconciled_transaction.from_dict(reconciled_transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


