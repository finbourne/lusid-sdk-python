# BatchAcceptMarginCallsRequest

Accepts several margin calls at their default agreed amounts, reporting the ones that could not be accepted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls** | [**List[MarginCallKey]**](MarginCallKey.md) | The calls to accept, each at its default agreed amount. A call that cannot be accepted is reported in failed and does not stop the others. | 
## Example

```python
from lusid.models.batch_accept_margin_calls_request import BatchAcceptMarginCallsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calls: List[MarginCallKey] = # Replace with your value
batch_accept_margin_calls_request_instance = BatchAcceptMarginCallsRequest(calls=calls)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

