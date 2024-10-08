# GroupReconciliationUserReview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_codes** | [**List[GroupReconciliationUserReviewBreakCode]**](GroupReconciliationUserReviewBreakCode.md) | A list of break codes shared between the reconciliation runs of the same run instance and result hash. | [optional] 
**match_keys** | [**List[GroupReconciliationUserReviewMatchKey]**](GroupReconciliationUserReviewMatchKey.md) | A list of match keys shared between the reconciliation runs of the same run instance and result hash. | [optional] 
**comments** | [**List[GroupReconciliationUserReviewComment]**](GroupReconciliationUserReviewComment.md) | A list of comments shared between the reconciliation runs of the same run instance and result hash. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review import GroupReconciliationUserReview

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReview from a JSON string
group_reconciliation_user_review_instance = GroupReconciliationUserReview.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReview.to_json()

# convert the object into a dict
group_reconciliation_user_review_dict = group_reconciliation_user_review_instance.to_dict()
# create an instance of GroupReconciliationUserReview from a dict
group_reconciliation_user_review_form_dict = group_reconciliation_user_review.from_dict(group_reconciliation_user_review_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


