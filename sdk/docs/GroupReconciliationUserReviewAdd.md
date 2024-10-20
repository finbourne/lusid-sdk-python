# GroupReconciliationUserReviewAdd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_code** | **str** | The break code of the reconciliation result. | [optional] 
**match_key** | **str** | The match key of the reconciliation result. | [optional] 
**comment_text** | **str** | User&#39;s comment regarding the reconciliation result. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review_add import GroupReconciliationUserReviewAdd

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReviewAdd from a JSON string
group_reconciliation_user_review_add_instance = GroupReconciliationUserReviewAdd.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReviewAdd.to_json()

# convert the object into a dict
group_reconciliation_user_review_add_dict = group_reconciliation_user_review_add_instance.to_dict()
# create an instance of GroupReconciliationUserReviewAdd from a dict
group_reconciliation_user_review_add_form_dict = group_reconciliation_user_review_add.from_dict(group_reconciliation_user_review_add_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


