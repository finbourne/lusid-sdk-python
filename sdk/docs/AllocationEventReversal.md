# AllocationEventReversal

How a booked Allocation Event was reversed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference the mirror postings were written under: the original booking reference with a -REV suffix. | [optional] 
**reason** | **str** | Why the event was reversed. | [optional] 
**reversed_at** | **datetime** | The datetime at which the event was reversed. | [optional] 
**effective_at** | **datetime** | The date the mirror postings were posted at. | [optional] 
**backdated** | **bool** | Whether the mirror postings were posted at the original event date despite the period being closed. | [optional] 
**refund_payable** | [**List[AllocationEventRefund]**](AllocationEventRefund.md) | Cash owed back to investors who had already paid in when the event was reversed. | [optional] 
## Example

```python
from lusid.models.allocation_event_reversal import AllocationEventReversal
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reference: Optional[StrictStr] = "example_reference"
reason: Optional[StrictStr] = "example_reason"
reversed_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
backdated: Optional[StrictBool] = # Replace with your value
backdated:Optional[StrictBool] = None
refund_payable: Optional[List[AllocationEventRefund]] = # Replace with your value
allocation_event_reversal_instance = AllocationEventReversal(reference=reference, reason=reason, reversed_at=reversed_at, effective_at=effective_at, backdated=backdated, refund_payable=refund_payable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

