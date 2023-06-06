# UpsertReconciliationBreakRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_fields** | **Dict[str, str]** | Fields for the left hand side of the reconciliation | [optional] 
**right_fields** | **Dict[str, str]** | Fields for the right hand side of the reconciliation | [optional] 
**diff** | **str** | The difference between two matching fields | [optional] 

## Example

```python
from lusid.models.upsert_reconciliation_break_request import UpsertReconciliationBreakRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReconciliationBreakRequest from a JSON string
upsert_reconciliation_break_request_instance = UpsertReconciliationBreakRequest.from_json(json)
# print the JSON string representation of the object
print UpsertReconciliationBreakRequest.to_json()

# convert the object into a dict
upsert_reconciliation_break_request_dict = upsert_reconciliation_break_request_instance.to_dict()
# create an instance of UpsertReconciliationBreakRequest from a dict
upsert_reconciliation_break_request_form_dict = upsert_reconciliation_break_request.from_dict(upsert_reconciliation_break_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


