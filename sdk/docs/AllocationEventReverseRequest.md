# AllocationEventReverseRequest

The request used to reverse a booked Allocation Event: why, and when the mirror postings are dated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the booked event is being reversed. | 
**effective_at** | **datetime** | The date to post the mirror entries at. Defaults to the original event date unless that period is closed, when it defaults to the current date. | [optional] 
**backdated** | **bool** | Whether to post the mirror entries at the original event date even when that period is closed. Defaults to false. | [optional] 
## Example

```python
from lusid.models.allocation_event_reverse_request import AllocationEventReverseRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reason: StrictStr = "example_reason"
effective_at: Optional[datetime] = # Replace with your value
backdated: Optional[StrictBool] = # Replace with your value
backdated:Optional[StrictBool] = None
allocation_event_reverse_request_instance = AllocationEventReverseRequest(reason=reason, effective_at=effective_at, backdated=backdated)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

