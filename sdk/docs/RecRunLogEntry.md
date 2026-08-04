# RecRunLogEntry

A single run within an instance's run log. All runs share the same effective dates (frozen at  instantiation); each has a different asAt, advanced on re-run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_number** | **int** | The run number within the instance. Increments with each re-run. | 
**run_as_at** | **datetime** | The asAt datetime at which the run happened. | 
**superseded_as_at** | **datetime** | The asAt datetime at which this run was superseded by a subsequent run. | [optional] 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
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
rec_run_log_entry_instance = RecRunLogEntry(run_number=run_number, run_as_at=run_as_at, superseded_as_at=superseded_as_at, dates_reconciled=dates_reconciled)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

