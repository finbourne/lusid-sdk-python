# GroupReconciliationUserReviewBreakCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_code** | **str** | The break code of the reconciliation result. | 
**user_id** | **str** | Id of the user who made a User Review input. | [optional] 
**as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**as_at_invalid** | **datetime** | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review_break_code import GroupReconciliationUserReviewBreakCode

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReviewBreakCode from a JSON string
group_reconciliation_user_review_break_code_instance = GroupReconciliationUserReviewBreakCode.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReviewBreakCode.to_json()

# convert the object into a dict
group_reconciliation_user_review_break_code_dict = group_reconciliation_user_review_break_code_instance.to_dict()
# create an instance of GroupReconciliationUserReviewBreakCode from a dict
group_reconciliation_user_review_break_code_form_dict = group_reconciliation_user_review_break_code.from_dict(group_reconciliation_user_review_break_code_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


