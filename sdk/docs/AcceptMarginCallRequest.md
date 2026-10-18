# AcceptMarginCallRequest

Accepts a margin call, at its default agreed amount or the amount given.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreed_amount** | **float** | The amount to accept. Optional when the call is matched or within tolerance, when our call or the counterparty&#39;s demand is taken; required when the demand breaks tolerance or has not been recorded. | [optional] 
## Example

```python
from lusid.models.accept_margin_call_request import AcceptMarginCallRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agreed_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accept_margin_call_request_instance = AcceptMarginCallRequest(agreed_amount=agreed_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

