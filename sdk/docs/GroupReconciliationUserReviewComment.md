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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
comment_text: StrictStr = "example_comment_text"
user_id: Optional[StrictStr] = "example_user_id"
as_at_added: Optional[datetime] = # Replace with your value
as_at_invalid: Optional[datetime] = # Replace with your value
group_reconciliation_user_review_comment_instance = GroupReconciliationUserReviewComment(comment_text=comment_text, user_id=user_id, as_at_added=as_at_added, as_at_invalid=as_at_invalid)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

