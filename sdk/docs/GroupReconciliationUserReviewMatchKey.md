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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

match_key: StrictStr = "example_match_key"
user_id: Optional[StrictStr] = "example_user_id"
as_at_added: Optional[datetime] = # Replace with your value
as_at_invalid: Optional[datetime] = # Replace with your value
group_reconciliation_user_review_match_key_instance = GroupReconciliationUserReviewMatchKey(match_key=match_key, user_id=user_id, as_at_added=as_at_added, as_at_invalid=as_at_invalid)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

