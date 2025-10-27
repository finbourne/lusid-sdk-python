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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

break_codes: Optional[List[GroupReconciliationUserReviewBreakCode]] = # Replace with your value
match_keys: Optional[List[GroupReconciliationUserReviewMatchKey]] = # Replace with your value
comments: Optional[List[GroupReconciliationUserReviewComment]] = # Replace with your value
group_reconciliation_user_review_instance = GroupReconciliationUserReview(break_codes=break_codes, match_keys=match_keys, comments=comments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

