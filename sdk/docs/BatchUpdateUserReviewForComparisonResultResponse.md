# BatchUpdateUserReviewForComparisonResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, GroupReconciliationComparisonResult]**](GroupReconciliationComparisonResult.md) | The collection of comparison results that have been successfully updated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The collection of comparison results that could not be updated with the provided user input along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to the updated comparison result user input | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.batch_update_user_review_for_comparison_result_response import BatchUpdateUserReviewForComparisonResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateUserReviewForComparisonResultResponse from a JSON string
batch_update_user_review_for_comparison_result_response_instance = BatchUpdateUserReviewForComparisonResultResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpdateUserReviewForComparisonResultResponse.to_json()

# convert the object into a dict
batch_update_user_review_for_comparison_result_response_dict = batch_update_user_review_for_comparison_result_response_instance.to_dict()
# create an instance of BatchUpdateUserReviewForComparisonResultResponse from a dict
batch_update_user_review_for_comparison_result_response_form_dict = batch_update_user_review_for_comparison_result_response.from_dict(batch_update_user_review_for_comparison_result_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


