# RecApprovalDecision

An entry in the append-only log of approver decisions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | The approval slot this decision satisfies. Must match a required approval code. | 
**decision** | **str** | The decision made. Available values: Approve, RequestRevisions. | 
**reason** | **str** | Rationale for the decision. | [optional] 
**user_id** | **str** | The approver who made the decision. | 
**as_at_decided** | **datetime** | The asAt datetime at which the decision was made. | 
**as_at_superseded** | **datetime** | The asAt datetime at which this entry was superseded. Null when it is the current standing entry. | [optional] 
## Example

```python
from lusid.models.rec_approval_decision import RecApprovalDecision
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

approval_code: StrictStr = "example_approval_code"
decision: StrictStr = "example_decision"
reason: Optional[StrictStr] = "example_reason"
user_id: StrictStr = "example_user_id"
as_at_decided: datetime = # Replace with your value
as_at_superseded: Optional[datetime] = # Replace with your value
rec_approval_decision_instance = RecApprovalDecision(approval_code=approval_code, decision=decision, reason=reason, user_id=user_id, as_at_decided=as_at_decided, as_at_superseded=as_at_superseded)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

