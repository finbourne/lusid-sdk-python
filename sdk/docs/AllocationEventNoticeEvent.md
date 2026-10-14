# AllocationEventNoticeEvent

The allocation event a notice is issued for.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the allocation event. | 
**event_date** | **datetime** | The effective date of the allocation event. | 
**notice_date** | **datetime** | The date the notice is issued. | [optional] 
**due_date** | **datetime** | The date the payment is due. | [optional] 
**status** | **str** | The status of the allocation event. | 
## Example

```python
from lusid.models.allocation_event_notice_event import AllocationEventNoticeEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
type: StrictStr = "example_type"
event_date: datetime = # Replace with your value
notice_date: Optional[datetime] = # Replace with your value
due_date: Optional[datetime] = # Replace with your value
status: StrictStr = "example_status"
allocation_event_notice_event_instance = AllocationEventNoticeEvent(id=id, type=type, event_date=event_date, notice_date=notice_date, due_date=due_date, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

