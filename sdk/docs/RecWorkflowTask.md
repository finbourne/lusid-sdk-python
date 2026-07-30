# RecWorkflowTask

The workflow service task that instantiated a rec instance.  Minimal placeholder until the full workflow service task DTO is available.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the workflow service task. | [optional] 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**state** | **str** | The current state of the workflow service task. | [optional] 
## Example

```python
from lusid.models.rec_workflow_task import RecWorkflowTask
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
task_definition_id: Optional[ResourceId] = # Replace with your value
state: Optional[StrictStr] = "example_state"
rec_workflow_task_instance = RecWorkflowTask(id=id, task_definition_id=task_definition_id, state=state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

