# DisputeMarginCallRequest

Disputes a margin call: moves the agreed amount now and leaves the rest of the demand in dispute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreed_amount** | **float** | The amount to move now; the rest of the counterparty&#39;s demand is left in dispute. | 
**reason** | **str** | Why the call is disputed. | 
**owner** | **str** | Who owns the dispute. Defaults to the caller if not specified. | [optional] 
## Example

```python
from lusid.models.dispute_margin_call_request import DisputeMarginCallRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agreed_amount: Union[StrictFloat, StrictInt] = # Replace with your value
reason: StrictStr = "example_reason"
owner: Optional[StrictStr] = "example_owner"
dispute_margin_call_request_instance = DisputeMarginCallRequest(agreed_amount=agreed_amount, reason=reason, owner=owner)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

