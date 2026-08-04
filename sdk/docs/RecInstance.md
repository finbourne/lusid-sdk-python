# RecInstance

The expanded view of a rec instance: its identity, lifecycle status, lock state, closed periods  (for Closed Period windows) and the time-series of runs in the run log.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**RecInstanceId**](RecInstanceId.md) |  | 
**rec_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**as_at_instantiated** | **datetime** | The asAt datetime at which the instance was first created. | 
**workflow_task_instantiated** | [**RecWorkflowTask**](RecWorkflowTask.md) |  | [optional] 
**status** | **str** | The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked. | 
**as_at_locked** | **datetime** | The wall-clock time the lock action was performed. Null when the instance has not been locked. | [optional] 
**dates_locked** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | [optional] 
**closed_periods** | [**RecClosedPeriods**](RecClosedPeriods.md) |  | [optional] 
**run_log** | [**List[RecRunLogEntry]**](RecRunLogEntry.md) | A chronologically ordered list of all runs on the instance. Always contains at least one entry. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.rec_instance import RecInstance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: RecInstanceId
rec_definition_id: ResourceId = # Replace with your value
as_at_instantiated: datetime = # Replace with your value
workflow_task_instantiated: Optional[RecWorkflowTask] = # Replace with your value
status: StrictStr = "example_status"
as_at_locked: Optional[datetime] = # Replace with your value
dates_locked: Optional[RecDatesReconciled] = # Replace with your value
closed_periods: Optional[RecClosedPeriods] = # Replace with your value
run_log: List[RecRunLogEntry] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
rec_instance_instance = RecInstance(id=id, rec_definition_id=rec_definition_id, as_at_instantiated=as_at_instantiated, workflow_task_instantiated=workflow_task_instantiated, status=status, as_at_locked=as_at_locked, dates_locked=dates_locked, closed_periods=closed_periods, run_log=run_log, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

