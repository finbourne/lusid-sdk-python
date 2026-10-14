# ProcessingGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. | 
**display_name** | **str** | The name of the Processing Group. | 
**description** | **str** | A description for the Processing Group. | [optional] 
**schedule** | [**ProcessingGroupSchedule**](ProcessingGroupSchedule.md) |  | 
**reference_list_id** | [**ResourceId**](ResourceId.md) |  | 
**workflow_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**list_exception_filter** | **str** | A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional. | [optional] 
## Example

```python
from lusid.models.processing_group_request import ProcessingGroupRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
schedule: ProcessingGroupSchedule
reference_list_id: ResourceId = # Replace with your value
workflow_id: Optional[ResourceId] = # Replace with your value
list_exception_filter: Optional[StrictStr] = "example_list_exception_filter"
processing_group_request_instance = ProcessingGroupRequest(code=code, display_name=display_name, description=description, schedule=schedule, reference_list_id=reference_list_id, workflow_id=workflow_id, list_exception_filter=list_exception_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

