# AllocationEventUnbookRequest

The request used to take a half-booked Allocation Event back to Computed, cancelling what it wrote.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the half-booked event is being taken back to Computed. | 
## Example

```python
from lusid.models.allocation_event_unbook_request import AllocationEventUnbookRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reason: StrictStr = "example_reason"
allocation_event_unbook_request_instance = AllocationEventUnbookRequest(reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

