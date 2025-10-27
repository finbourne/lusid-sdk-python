# CancelledOrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_state** | [**Order**](Order.md) |  | [optional] 
## Example

```python
from lusid.models.cancelled_order_result import CancelledOrderResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_state: Optional[Order] = # Replace with your value
cancelled_order_result_instance = CancelledOrderResult(order_state=order_state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

