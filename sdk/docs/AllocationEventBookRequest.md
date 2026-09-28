# AllocationEventBookRequest

The request used to book a computed Allocation Event: the reference under which its shares were posted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_reference** | **str** | The reference under which the computed shares were posted, for instance a journal entry code. | 
## Example

```python
from lusid.models.allocation_event_book_request import AllocationEventBookRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

booking_reference: StrictStr = "example_booking_reference"
allocation_event_book_request_instance = AllocationEventBookRequest(booking_reference=booking_reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

