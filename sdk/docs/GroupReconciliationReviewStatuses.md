# GroupReconciliationReviewStatuses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_pending** | **int** | The number of comparison results of reviewStatus \&quot;Pending\&quot; with this instanceId and reconciliationType | 
**link_pending** | [**Link**](Link.md) |  | 
**count_reviewed** | **int** | The number of comparison results of reviewStatus \&quot;Reviewed\&quot; with this instanceId and reconciliationType | 
**link_reviewed** | [**Link**](Link.md) |  | 
**count_matched** | **int** | The number of comparison results of reviewStatus \&quot;Matched\&quot; with this instanceId and reconciliationType | 
**link_matched** | [**Link**](Link.md) |  | 
**count_invalid** | **int** | The number of comparison results of reviewStatus \&quot;Invalid\&quot; with this instanceId and reconciliationType | 
**link_invalid** | [**Link**](Link.md) |  | 

## Example

```python
from lusid.models.group_reconciliation_review_statuses import GroupReconciliationReviewStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationReviewStatuses from a JSON string
group_reconciliation_review_statuses_instance = GroupReconciliationReviewStatuses.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationReviewStatuses.to_json()

# convert the object into a dict
group_reconciliation_review_statuses_dict = group_reconciliation_review_statuses_instance.to_dict()
# create an instance of GroupReconciliationReviewStatuses from a dict
group_reconciliation_review_statuses_form_dict = group_reconciliation_review_statuses.from_dict(group_reconciliation_review_statuses_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


