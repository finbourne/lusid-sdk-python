# GroupReconciliationRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Reconciliation run Id. Consists of run type (manual or workflow) and identifier. | 
**dates_to_reconcile** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_run_request import GroupReconciliationRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationRunRequest from a JSON string
group_reconciliation_run_request_instance = GroupReconciliationRunRequest.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationRunRequest.to_json()

# convert the object into a dict
group_reconciliation_run_request_dict = group_reconciliation_run_request_instance.to_dict()
# create an instance of GroupReconciliationRunRequest from a dict
group_reconciliation_run_request_form_dict = group_reconciliation_run_request.from_dict(group_reconciliation_run_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


