# TransactionReconciliationRequest

Specifies the parameter to be use when performing a Transaction Reconciliation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**right_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**from_transaction_date** | **datetime** |  | 
**to_transaction_date** | **datetime** |  | 
**as_at** | **datetime** |  | [optional] 
**property_keys** | **List[str]** |  | [optional] 

## Example

```python
from lusid.models.transaction_reconciliation_request import TransactionReconciliationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReconciliationRequest from a JSON string
transaction_reconciliation_request_instance = TransactionReconciliationRequest.from_json(json)
# print the JSON string representation of the object
print TransactionReconciliationRequest.to_json()

# convert the object into a dict
transaction_reconciliation_request_dict = transaction_reconciliation_request_instance.to_dict()
# create an instance of TransactionReconciliationRequest from a dict
transaction_reconciliation_request_form_dict = transaction_reconciliation_request.from_dict(transaction_reconciliation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


