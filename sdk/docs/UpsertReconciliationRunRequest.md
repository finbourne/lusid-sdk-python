# UpsertReconciliationRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The effective date of the reconciliation run | 
**version** | **int** | The version number for a run | 

## Example

```python
from lusid.models.upsert_reconciliation_run_request import UpsertReconciliationRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReconciliationRunRequest from a JSON string
upsert_reconciliation_run_request_instance = UpsertReconciliationRunRequest.from_json(json)
# print the JSON string representation of the object
print UpsertReconciliationRunRequest.to_json()

# convert the object into a dict
upsert_reconciliation_run_request_dict = upsert_reconciliation_run_request_instance.to_dict()
# create an instance of UpsertReconciliationRunRequest from a dict
upsert_reconciliation_run_request_form_dict = upsert_reconciliation_run_request.from_dict(upsert_reconciliation_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


