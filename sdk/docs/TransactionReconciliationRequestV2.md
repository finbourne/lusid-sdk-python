# TransactionReconciliationRequestV2

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of transactions from a portfolio  The results of this can then be compared to each other.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**AggregatedTransactionsRequest**](AggregatedTransactionsRequest.md) |  | 
**right** | [**AggregatedTransactionsRequest**](AggregatedTransactionsRequest.md) |  | 
**left_to_right_mapping** | [**List[ReconciliationLeftRightAddressKeyPair]**](ReconciliationLeftRightAddressKeyPair.md) | The mapping from property keys requested by left aggregation to property keys on right hand side | [optional] 
**comparison_rules** | [**List[ReconciliationRule]**](ReconciliationRule.md) | The set of rules to be used in comparing values. These are the rules that determine what constitutes a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types. | [optional] 
**preserve_keys** | **List[str]** | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results). | [optional] 

## Example

```python
from lusid.models.transaction_reconciliation_request_v2 import TransactionReconciliationRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReconciliationRequestV2 from a JSON string
transaction_reconciliation_request_v2_instance = TransactionReconciliationRequestV2.from_json(json)
# print the JSON string representation of the object
print TransactionReconciliationRequestV2.to_json()

# convert the object into a dict
transaction_reconciliation_request_v2_dict = transaction_reconciliation_request_v2_instance.to_dict()
# create an instance of TransactionReconciliationRequestV2 from a dict
transaction_reconciliation_request_v2_form_dict = transaction_reconciliation_request_v2.from_dict(transaction_reconciliation_request_v2_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


