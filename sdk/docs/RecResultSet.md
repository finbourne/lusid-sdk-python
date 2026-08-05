# RecResultSet

The collection of reconciliation results for a given rec type within a rec instance. Identified by  its rec type and instance. The latest run's data is promoted to the root; prior runs are available  via previousRuns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_type** | **str** | The type of rec that this result set belongs to (e.g. Holding). Together with the rec instance, this uniquely identifies the result set. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. | 
**rec_instance** | [**RecInstanceSummary**](RecInstanceSummary.md) |  | 
**run_number** | **int** | The run number within the instance. Increments with each re-run. | 
**run_as_at** | **datetime** | The asAt datetime at which the run happened. | 
**execution** | [**RecExecution**](RecExecution.md) |  | 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
**result_counts** | [**RecResultCounts**](RecResultCounts.md) |  | 
**review** | [**RecReview**](RecReview.md) |  | 
**approval_status** | **str** | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. | 
**required_approvals** | [**List[RecRequiredApproval]**](RecRequiredApproval.md) | The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty. | 
**submissions** | [**List[RecSubmission]**](RecSubmission.md) | An append-only log of review submissions. May be empty. | 
**decisions** | [**List[RecApprovalDecision]**](RecApprovalDecision.md) | An append-only log of approver decisions. May be empty. | 
**previous_runs** | [**List[RecSupersededRun]**](RecSupersededRun.md) | Prior run snapshots, each frozen at the point of re-run. Populated only when includePreviousRuns is true. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.rec_result_set import RecResultSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_type: StrictStr = "example_rec_type"
rec_instance: RecInstanceSummary = # Replace with your value
run_number: StrictInt = # Replace with your value
run_number: StrictInt = 42
run_as_at: datetime = # Replace with your value
execution: RecExecution
dates_reconciled: RecDatesReconciled = # Replace with your value
result_counts: RecResultCounts = # Replace with your value
review: RecReview
approval_status: StrictStr = "example_approval_status"
required_approvals: List[RecRequiredApproval] = # Replace with your value
submissions: List[RecSubmission] = # Replace with your value
decisions: List[RecApprovalDecision] = # Replace with your value
previous_runs: List[RecSupersededRun] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
rec_result_set_instance = RecResultSet(rec_type=rec_type, rec_instance=rec_instance, run_number=run_number, run_as_at=run_as_at, execution=execution, dates_reconciled=dates_reconciled, result_counts=result_counts, review=review, approval_status=approval_status, required_approvals=required_approvals, submissions=submissions, decisions=decisions, previous_runs=previous_runs, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

