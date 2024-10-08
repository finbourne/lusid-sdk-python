# GroupReconciliationUserReviewComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_text** | **str** | User&#39;s comment regarding the reconciliation result. | 
**user_id** | **str** | Id of the user who made a User Review input. | [optional] 
**as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**as_at_invalid** | **datetime** | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review_comment import GroupReconciliationUserReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReviewComment from a JSON string
group_reconciliation_user_review_comment_instance = GroupReconciliationUserReviewComment.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReviewComment.to_json()

# convert the object into a dict
group_reconciliation_user_review_comment_dict = group_reconciliation_user_review_comment_instance.to_dict()
# create an instance of GroupReconciliationUserReviewComment from a dict
group_reconciliation_user_review_comment_form_dict = group_reconciliation_user_review_comment.from_dict(group_reconciliation_user_review_comment_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


