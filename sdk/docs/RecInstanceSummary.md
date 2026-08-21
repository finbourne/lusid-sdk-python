# RecInstanceSummary

A lightweight view of the rec instance, nested on each result set. It carries the instance-level  status, which is how a result set surfaces the instance's running/locked state to the dashboard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**RecInstanceId**](RecInstanceId.md) |  | 
**rec_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**as_at_instantiated** | **datetime** | The asAt datetime at which the instance was first created. | 
**status** | **str** | The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked. | 
**as_at_locked** | **datetime** | The wall-clock time the lock action was performed. Null when the instance has not been locked. | [optional] 
## Example

```python
from lusid.models.rec_instance_summary import RecInstanceSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: RecInstanceId
rec_definition_id: ResourceId = # Replace with your value
as_at_instantiated: datetime = # Replace with your value
status: StrictStr = "example_status"
as_at_locked: Optional[datetime] = # Replace with your value
rec_instance_summary_instance = RecInstanceSummary(id=id, rec_definition_id=rec_definition_id, as_at_instantiated=as_at_instantiated, status=status, as_at_locked=as_at_locked)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

