# StagedModificationDecision

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | Time the decision request is made. | [optional] 
**user_id** | **str** | ID of user that approved the request. | [optional] 
**request_id** | **str** | ID of user that made the request. | [optional] 
**decision** | **str** | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. | [optional] 
**comment** | **str** | Comment on decision. | [optional] 
## Example

```python
from lusid.models.staged_modification_decision import StagedModificationDecision
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
as_at: Optional[datetime] = # Replace with your value
user_id: Optional[StrictStr] = "example_user_id"
request_id: Optional[StrictStr] = "example_request_id"
decision: Optional[StrictStr] = "example_decision"
comment: Optional[StrictStr] = "example_comment"
staged_modification_decision_instance = StagedModificationDecision(as_at=as_at, user_id=user_id, request_id=request_id, decision=decision, comment=comment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

