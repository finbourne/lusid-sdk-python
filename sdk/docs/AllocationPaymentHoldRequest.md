# AllocationPaymentHoldRequest

The request used to place, move or release a hold on a partner's payment against an allocation event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The hold status to set: Blocked, Escrow or Released. A hold may only be released by a different user from the one who placed it. | 
**reason** | **str** | The reason for the hold. | [optional] 
**reference** | **str** | An external reference for the hold, such as a compliance case number. | [optional] 
## Example

```python
from lusid.models.allocation_payment_hold_request import AllocationPaymentHoldRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
reason: Optional[StrictStr] = "example_reason"
reference: Optional[StrictStr] = "example_reference"
allocation_payment_hold_request_instance = AllocationPaymentHoldRequest(status=status, reason=reason, reference=reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

