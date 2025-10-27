# GroupReconciliationUserReviewRemove

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_code_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**match_key_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
**comment_text_as_at_added** | **datetime** | The timestamp of the added User Review input. | [optional] 
## Example

```python
from lusid.models.group_reconciliation_user_review_remove import GroupReconciliationUserReviewRemove
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

break_code_as_at_added: Optional[datetime] = # Replace with your value
match_key_as_at_added: Optional[datetime] = # Replace with your value
comment_text_as_at_added: Optional[datetime] = # Replace with your value
group_reconciliation_user_review_remove_instance = GroupReconciliationUserReviewRemove(break_code_as_at_added=break_code_as_at_added, match_key_as_at_added=match_key_as_at_added, comment_text_as_at_added=comment_text_as_at_added)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

