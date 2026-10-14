# AllocationPaymentHold

A hold placed on a partner's payment against an allocation event, blocking receipt until it is released  by a second user.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_event_id** | [**ResourceId**](ResourceId.md) |  | 
**investor_record_id** | **str** | The investor record identifier of the partner whose payment is held. | 
**status** | **str** | The hold status: Blocked, Escrow or Released. | 
**reason** | **str** | The reason for the hold. | [optional] 
**reference** | **str** | An external reference for the hold, such as a compliance case number. | [optional] 
**placed_by** | **str** | The user who placed the hold. | 
**placed_at** | **datetime** | When the hold was placed. | 
**released_by** | **str** | The user who released the hold, or null while it is active. | [optional] 
**released_at** | **datetime** | When the hold was released, or null while it is active. | [optional] 
**active** | **bool** | Whether the hold is currently blocking receipt of the partner&#39;s payment. | 
## Example

```python
from lusid.models.allocation_payment_hold import AllocationPaymentHold
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allocation_event_id: ResourceId = # Replace with your value
investor_record_id: StrictStr = "example_investor_record_id"
status: StrictStr = "example_status"
reason: Optional[StrictStr] = "example_reason"
reference: Optional[StrictStr] = "example_reference"
placed_by: StrictStr = "example_placed_by"
placed_at: datetime = # Replace with your value
released_by: Optional[StrictStr] = "example_released_by"
released_at: Optional[datetime] = # Replace with your value
active: StrictBool = # Replace with your value
active:StrictBool = True
allocation_payment_hold_instance = AllocationPaymentHold(allocation_event_id=allocation_event_id, investor_record_id=investor_record_id, status=status, reason=reason, reference=reference, placed_by=placed_by, placed_at=placed_at, released_by=released_by, released_at=released_at, active=active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

