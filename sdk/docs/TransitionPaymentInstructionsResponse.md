# TransitionPaymentInstructionsResponse

The response from transitioning the status of a set of Payment Instructions. Each request key from the  incoming map appears in exactly one of Values or Failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, PaymentInstruction]**](PaymentInstruction.md) | The Payment Instructions that were transitioned successfully, at their new status, keyed by the ephemeral request key supplied by the caller. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | Details of the requested transitions that failed, keyed by the ephemeral request key supplied by the caller. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transition_payment_instructions_response import TransitionPaymentInstructionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, PaymentInstruction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
transition_payment_instructions_response_instance = TransitionPaymentInstructionsResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

