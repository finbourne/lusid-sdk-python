# AllocationRegisterReceivable

What one register is owed on a booked capital call, across every record called on its lines.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**called** | **float** | What was called on the register&#39;s lines. | [optional] 
**received** | **float** | What has settled the register&#39;s lines so far. | [optional] 
**outstanding** | **float** | What the register is still owed. | [optional] 
## Example

```python
from lusid.models.allocation_register_receivable import AllocationRegisterReceivable
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio: Optional[ResourceId] = None
called: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
received: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
outstanding: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
allocation_register_receivable_instance = AllocationRegisterReceivable(portfolio=portfolio, called=called, received=received, outstanding=outstanding)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

