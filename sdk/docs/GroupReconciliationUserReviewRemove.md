# GroupReconciliationUserReviewRemove


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_code_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**match_key_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**comment_text_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review_remove import GroupReconciliationUserReviewRemove

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReviewRemove from a JSON string
group_reconciliation_user_review_remove_instance = GroupReconciliationUserReviewRemove.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReviewRemove.to_json()

# convert the object into a dict
group_reconciliation_user_review_remove_dict = group_reconciliation_user_review_remove_instance.to_dict()
# create an instance of GroupReconciliationUserReviewRemove from a dict
group_reconciliation_user_review_remove_form_dict = group_reconciliation_user_review_remove.from_dict(group_reconciliation_user_review_remove_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


