# RecRunLog

One rec type's run history within a rec instance: its most recent runs, and the total number of runs those  were taken from.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_count** | **int** | The total number of runs of this rec type, which is not necessarily the number returned. A value greater than ten means runs has been truncated; the runs beyond it remain retrievable from previousRuns on the rec type&#39;s result set. | 
**runs** | [**List[RecRunLogEntry]**](RecRunLogEntry.md) | The ten most recent runs of this rec type, ordered by run number descending, so the current run is always the first entry. Exactly one entry has a null supersededAsAt. | 
## Example

```python
from lusid.models.rec_run_log import RecRunLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_count: StrictInt = # Replace with your value
run_count: StrictInt = 42
runs: List[RecRunLogEntry] = # Replace with your value
rec_run_log_instance = RecRunLog(run_count=run_count, runs=runs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

