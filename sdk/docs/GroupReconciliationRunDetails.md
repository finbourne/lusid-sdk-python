# GroupReconciliationRunDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_status** | **str** | Provides the reconciliation completion status \&quot;Completed\&quot; | \&quot;FailedToComplete\&quot; | 
**error_detail** | **str** | Error information if the reconciliation failed to complete | [optional] 

## Example

```python
from lusid.models.group_reconciliation_run_details import GroupReconciliationRunDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationRunDetails from a JSON string
group_reconciliation_run_details_instance = GroupReconciliationRunDetails.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationRunDetails.to_json()

# convert the object into a dict
group_reconciliation_run_details_dict = group_reconciliation_run_details_instance.to_dict()
# create an instance of GroupReconciliationRunDetails from a dict
group_reconciliation_run_details_form_dict = group_reconciliation_run_details.from_dict(group_reconciliation_run_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


