# RecSupersededRun

A prior run snapshot, frozen at the point of re-run. Has the same shape as the root-level run  fields on the result set, plus the asAt at which the run was superseded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_number** | **int** | The run number within the instance. Increments with each re-run. | 
**run_as_at** | **datetime** | The asAt datetime at which the run happened. | 
**superseded_as_at** | **datetime** | The asAt datetime at which this run was superseded by a subsequent run. | 
**execution** | [**RecExecution**](RecExecution.md) |  | 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
**result_counts** | [**RecResultCounts**](RecResultCounts.md) |  | 
**review** | [**RecReview**](RecReview.md) |  | 
**approval_status** | **str** | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. | 
**required_approvals** | [**List[RecRequiredApproval]**](RecRequiredApproval.md) | The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty. | 
**submissions** | [**List[RecSubmission]**](RecSubmission.md) | An append-only log of review submissions. May be empty. | 
**decisions** | [**List[RecApprovalDecision]**](RecApprovalDecision.md) | An append-only log of approver decisions. May be empty. | 
## Example

```python
from lusid.models.rec_superseded_run import RecSupersededRun
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_number: StrictInt = # Replace with your value
run_number: StrictInt = 42
run_as_at: datetime = # Replace with your value
superseded_as_at: datetime = # Replace with your value
execution: RecExecution
dates_reconciled: RecDatesReconciled = # Replace with your value
result_counts: RecResultCounts = # Replace with your value
review: RecReview
approval_status: StrictStr = "example_approval_status"
required_approvals: List[RecRequiredApproval] = # Replace with your value
submissions: List[RecSubmission] = # Replace with your value
decisions: List[RecApprovalDecision] = # Replace with your value
rec_superseded_run_instance = RecSupersededRun(run_number=run_number, run_as_at=run_as_at, superseded_as_at=superseded_as_at, execution=execution, dates_reconciled=dates_reconciled, result_counts=result_counts, review=review, approval_status=approval_status, required_approvals=required_approvals, submissions=submissions, decisions=decisions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

