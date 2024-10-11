# GroupReconciliationResultStatuses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_new** | **int** | The number of comparison results of resultStatus \&quot;New\&quot; with this instanceId and reconciliationType | 
**link_new** | [**Link**](Link.md) |  | 
**count_confirmed** | **int** | The number of comparison results of resultStatus \&quot;Confirmed\&quot; with this instanceId and reconciliationType | 
**link_confirmed** | [**Link**](Link.md) |  | 
**count_changed** | **int** | The number of comparison results of resultStatus \&quot;Changed\&quot; with this instanceId and reconciliationType | 
**link_changed** | [**Link**](Link.md) |  | 

## Example

```python
from lusid.models.group_reconciliation_result_statuses import GroupReconciliationResultStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationResultStatuses from a JSON string
group_reconciliation_result_statuses_instance = GroupReconciliationResultStatuses.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationResultStatuses.to_json()

# convert the object into a dict
group_reconciliation_result_statuses_dict = group_reconciliation_result_statuses_instance.to_dict()
# create an instance of GroupReconciliationResultStatuses from a dict
group_reconciliation_result_statuses_form_dict = group_reconciliation_result_statuses.from_dict(group_reconciliation_result_statuses_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


