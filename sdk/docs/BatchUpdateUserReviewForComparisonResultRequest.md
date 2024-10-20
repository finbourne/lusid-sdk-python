# BatchUpdateUserReviewForComparisonResultRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_result_id** | **str** | Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId. | 
**user_review_add** | [**GroupReconciliationUserReviewAdd**](GroupReconciliationUserReviewAdd.md) |  | [optional] 
**user_review_remove** | [**GroupReconciliationUserReviewRemove**](GroupReconciliationUserReviewRemove.md) |  | [optional] 

## Example

```python
from lusid.models.batch_update_user_review_for_comparison_result_request import BatchUpdateUserReviewForComparisonResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateUserReviewForComparisonResultRequest from a JSON string
batch_update_user_review_for_comparison_result_request_instance = BatchUpdateUserReviewForComparisonResultRequest.from_json(json)
# print the JSON string representation of the object
print BatchUpdateUserReviewForComparisonResultRequest.to_json()

# convert the object into a dict
batch_update_user_review_for_comparison_result_request_dict = batch_update_user_review_for_comparison_result_request_instance.to_dict()
# create an instance of BatchUpdateUserReviewForComparisonResultRequest from a dict
batch_update_user_review_for_comparison_result_request_form_dict = batch_update_user_review_for_comparison_result_request.from_dict(batch_update_user_review_for_comparison_result_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


