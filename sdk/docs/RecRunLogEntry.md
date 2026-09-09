# RecRunLogEntry

A summary of a single run of a single rec type within an instance's run log, carrying the per-run outcome  detail the grouped-by-instance overview renders. Every entry comes off a result set, so only a run that has  completed or failed appears: a run still in flight is not logged until it lands.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_number** | **int** | The run number within the instance. Increments with each re-run. | 
**run_as_at** | **datetime** | The asAt datetime at which the run happened. | 
**superseded_as_at** | **datetime** | The asAt datetime at which this run was superseded by a subsequent run. | [optional] 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
**execution** | [**RecExecution**](RecExecution.md) |  | 
**approval_status** | **str** | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. | 
**result_counts** | [**RecResultCounts**](RecResultCounts.md) |  | [optional] 
**review** | [**RecReview**](RecReview.md) |  | [optional] 
**rec_result_set_href** | **str** | The specific Uniform Resource Identifier (URI) of the full rec result set this run belongs to. | 
## Example

```python
from lusid.models.rec_run_log_entry import RecRunLogEntry
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_number: StrictInt = # Replace with your value
run_number: StrictInt = 42
run_as_at: datetime = # Replace with your value
superseded_as_at: Optional[datetime] = # Replace with your value
dates_reconciled: RecDatesReconciled = # Replace with your value
execution: RecExecution
approval_status: StrictStr = "example_approval_status"
result_counts: Optional[RecResultCounts] = # Replace with your value
review: Optional[RecReview] = None
rec_result_set_href: StrictStr = "example_rec_result_set_href"
rec_run_log_entry_instance = RecRunLogEntry(run_number=run_number, run_as_at=run_as_at, superseded_as_at=superseded_as_at, dates_reconciled=dates_reconciled, execution=execution, approval_status=approval_status, result_counts=result_counts, review=review, rec_result_set_href=rec_result_set_href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

