# PaymentInstructionStatus

The current status of a Payment Instruction. Managed exclusively via the dedicated  status transition API — not accepted on upsert.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_value** | **str** | The current status value. One of: Created, Staged, Released, Instructed, Sent, Cancelled. | 
**as_at_last_transition** | **datetime** | The as-at timestamp of the most recent status transition. | 
**user_id_last_transition** | **str** | The ID of the user who made the most recent status transition. | 
## Example

```python
from lusid.models.payment_instruction_status import PaymentInstructionStatus
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

current_value: StrictStr = "example_current_value"
as_at_last_transition: datetime = # Replace with your value
user_id_last_transition: StrictStr = "example_user_id_last_transition"
payment_instruction_status_instance = PaymentInstructionStatus(current_value=current_value, as_at_last_transition=as_at_last_transition, user_id_last_transition=user_id_last_transition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

