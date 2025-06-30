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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

break_codes: Optional[conlist(GroupReconciliationUserReviewBreakCode)] = # Replace with your value
match_keys: Optional[conlist(GroupReconciliationUserReviewMatchKey)] = # Replace with your value
comments: Optional[conlist(GroupReconciliationUserReviewComment)] = # Replace with your value
group_reconciliation_user_review_instance = GroupReconciliationUserReview(break_codes=break_codes, match_keys=match_keys, comments=comments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

