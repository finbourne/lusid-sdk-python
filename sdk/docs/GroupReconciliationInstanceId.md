# GroupReconciliationInstanceId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id_type** | **str** | Type of the reconciliation run, manual or automatic (via the workflow). \&quot;Manual\&quot; | \&quot;WorkflowServiceTaskId\&quot; | 
**run_id_value** | **str** | Reconciliation run identifier: a manually-provided key or taskId. | 

## Example

```python
from lusid.models.group_reconciliation_instance_id import GroupReconciliationInstanceId

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationInstanceId from a JSON string
group_reconciliation_instance_id_instance = GroupReconciliationInstanceId.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationInstanceId.to_json()

# convert the object into a dict
group_reconciliation_instance_id_dict = group_reconciliation_instance_id_instance.to_dict()
# create an instance of GroupReconciliationInstanceId from a dict
group_reconciliation_instance_id_form_dict = group_reconciliation_instance_id.from_dict(group_reconciliation_instance_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


