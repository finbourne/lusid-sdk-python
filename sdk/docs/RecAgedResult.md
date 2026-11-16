# RecAgedResult

A summary of a rec result in another instance, as at the stamp that first recorded it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the result within its instance, e.g. &#39;Holding-break-1&#39;. With instanceId, it fully qualifies the result. | 
**instance_id** | [**RecInstanceId**](RecInstanceId.md) |  | 
**run_number** | **int** | The result&#39;s latest run as at the stamp that first recorded it. | 
**run_as_at** | **datetime** | The asAt datetime of the result&#39;s latest run as at the stamp that first recorded it. | 
**first_run_seen** | **int** | The run in which the result was first assigned its id. | 
**as_at_first_seen** | **datetime** | The runAsAt of the run in which the result first appeared in its instance, the run numbered firstRunSeen. Written once: re-runs leave it unchanged. | 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
**exception_status** | **str** | The result&#39;s exception status as at the stamp that first recorded it: Open or Closed. Available values: Open, Closed. | 
**closure_type** | **str** | The result&#39;s exception closure type as at the stamp that first recorded it. Null while the exception is open. Available values: Cleared, Accepted, ForceMatched. | [optional] 
## Example

```python
from lusid.models.rec_aged_result import RecAgedResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
instance_id: RecInstanceId = # Replace with your value
run_number: StrictInt = # Replace with your value
run_number: StrictInt = 42
run_as_at: datetime = # Replace with your value
first_run_seen: StrictInt = # Replace with your value
first_run_seen: StrictInt = 42
as_at_first_seen: datetime = # Replace with your value
dates_reconciled: RecDatesReconciled = # Replace with your value
exception_status: StrictStr = "example_exception_status"
closure_type: Optional[StrictStr] = "example_closure_type"
rec_aged_result_instance = RecAgedResult(id=id, instance_id=instance_id, run_number=run_number, run_as_at=run_as_at, first_run_seen=first_run_seen, as_at_first_seen=as_at_first_seen, dates_reconciled=dates_reconciled, exception_status=exception_status, closure_type=closure_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

