# RecResultSetApprovalDecisionRequest

The request for an approver to approve a submitted review or request revisions. Each call satisfies  (or rejects) one approval slot from the result set's required approvals.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | The approval slot being decided. Must match a required approval code. | 
**decision** | **str** | The decision made. Available values: Approve, RequestRevisions. | 
**reason** | **str** | Rationale for the decision. | [optional] 
**requested_result_revisions** | [**List[RecRequestedResultRevision]**](RecRequestedResultRevision.md) | The results flagged for re-review. Only applicable when the decision is Request Revisions. | [optional] 
## Example

```python
from lusid.models.rec_result_set_approval_decision_request import RecResultSetApprovalDecisionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

approval_code: StrictStr = "example_approval_code"
decision: StrictStr = "example_decision"
reason: Optional[StrictStr] = "example_reason"
requested_result_revisions: Optional[List[RecRequestedResultRevision]] = # Replace with your value
rec_result_set_approval_decision_request_instance = RecResultSetApprovalDecisionRequest(approval_code=approval_code, decision=decision, reason=reason, requested_result_revisions=requested_result_revisions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

