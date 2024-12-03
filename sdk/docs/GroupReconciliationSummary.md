# GroupReconciliationSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_details** | [**GroupReconciliationRunDetails**](GroupReconciliationRunDetails.md) |  | [optional] 
**group_reconciliation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**instance_id** | [**GroupReconciliationInstanceId**](GroupReconciliationInstanceId.md) |  | 
**dates_reconciled** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | 
**reconciliation_run_as_at** | **datetime** | The date and time the reconciliation was run | 
**count_comparison_results** | **int** | The total number of comparison results with this InstanceId and ReconciliationType | 
**link_comparison_results** | [**Link**](Link.md) |  | [optional] 
**result_types** | [**GroupReconciliationResultTypes**](GroupReconciliationResultTypes.md) |  | [optional] 
**result_statuses** | [**GroupReconciliationResultStatuses**](GroupReconciliationResultStatuses.md) |  | [optional] 
**review_statuses** | [**GroupReconciliationReviewStatuses**](GroupReconciliationReviewStatuses.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_summary import GroupReconciliationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationSummary from a JSON string
group_reconciliation_summary_instance = GroupReconciliationSummary.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationSummary.to_json()

# convert the object into a dict
group_reconciliation_summary_dict = group_reconciliation_summary_instance.to_dict()
# create an instance of GroupReconciliationSummary from a dict
group_reconciliation_summary_form_dict = group_reconciliation_summary.from_dict(group_reconciliation_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


