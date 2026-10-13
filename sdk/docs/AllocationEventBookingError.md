# AllocationEventBookingError

One posting a booking could not write.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The rule or write step that failed, for instance WriteFailed. | [optional] 
**id** | **str** | The identifier of the posting that could not be written. | [optional] 
**message** | **str** | What went wrong. | [optional] 
## Example

```python
from lusid.models.allocation_event_booking_error import AllocationEventBookingError
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
id: Optional[StrictStr] = "example_id"
message: Optional[StrictStr] = "example_message"
allocation_event_booking_error_instance = AllocationEventBookingError(code=code, id=id, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

