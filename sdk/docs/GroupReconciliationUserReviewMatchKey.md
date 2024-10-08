# GroupReconciliationUserReviewMatchKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_key** | **str** | The match key of the reconciliation result. | 
**user_id** | **str** | Id of the user who made a User Review input. | [optional] 
**as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**as_at_invalid** | **datetime** | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. | [optional] 

## Example

```python
from lusid.models.group_reconciliation_user_review_match_key import GroupReconciliationUserReviewMatchKey

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationUserReviewMatchKey from a JSON string
group_reconciliation_user_review_match_key_instance = GroupReconciliationUserReviewMatchKey.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationUserReviewMatchKey.to_json()

# convert the object into a dict
group_reconciliation_user_review_match_key_dict = group_reconciliation_user_review_match_key_instance.to_dict()
# create an instance of GroupReconciliationUserReviewMatchKey from a dict
group_reconciliation_user_review_match_key_form_dict = group_reconciliation_user_review_match_key.from_dict(group_reconciliation_user_review_match_key_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


