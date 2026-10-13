# AllocationEventBookingWarning

One validation rule a booking was allowed to proceed through under the map's policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The rule that was allowed through, for instance OverCall. | [optional] 
**detail** | **str** | What the rule found. | [optional] 
## Example

```python
from lusid.models.allocation_event_booking_warning import AllocationEventBookingWarning
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
detail: Optional[StrictStr] = "example_detail"
allocation_event_booking_warning_instance = AllocationEventBookingWarning(code=code, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

