# BatchAcceptMarginCallsResponse

The outcome of accepting several margin calls: those accepted, and those refused with the reason.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[MarginCall]**](MarginCall.md) | The calls that were accepted. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The calls that could not be accepted, keyed by call id, with the reason. | 
## Example

```python
from lusid.models.batch_accept_margin_calls_response import BatchAcceptMarginCallsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[MarginCall] = # Replace with your value
failed: Dict[str, ErrorDetail] = # Replace with your value
batch_accept_margin_calls_response_instance = BatchAcceptMarginCallsResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

