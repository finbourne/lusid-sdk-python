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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

comparison_result_id: StrictStr = "example_comparison_result_id"
user_review_add: Optional[GroupReconciliationUserReviewAdd] = # Replace with your value
user_review_remove: Optional[GroupReconciliationUserReviewRemove] = # Replace with your value
batch_update_user_review_for_comparison_result_request_instance = BatchUpdateUserReviewForComparisonResultRequest(comparison_result_id=comparison_result_id, user_review_add=user_review_add, user_review_remove=user_review_remove)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

