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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

break_code: Optional[StrictStr] = "example_break_code"
match_key: Optional[StrictStr] = "example_match_key"
comment_text: Optional[StrictStr] = "example_comment_text"
group_reconciliation_user_review_add_instance = GroupReconciliationUserReviewAdd(break_code=break_code, match_key=match_key, comment_text=comment_text)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

