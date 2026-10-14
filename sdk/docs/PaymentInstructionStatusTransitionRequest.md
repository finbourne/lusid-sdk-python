# PaymentInstructionStatusTransitionRequest

A request to move one Payment Instruction to a new status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**status** | **str** | The status to move the Payment Instruction to. One of: Created, Staged, Released, Instructed, Sent, Cancelled, Failed. The transition must be permitted from the instruction&#39;s current status. Available values: Created, Staged, Released, Instructed, Sent, Cancelled, Failed. | 
## Example

```python
from lusid.models.payment_instruction_status_transition_request import PaymentInstructionStatusTransitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
status: StrictStr = "example_status"
payment_instruction_status_transition_request_instance = PaymentInstructionStatusTransitionRequest(id=id, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

