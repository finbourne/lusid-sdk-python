# OrderInstructionSetRequest

A request to create or update multiple OrderInstructions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[OrderInstructionRequest]**](OrderInstructionRequest.md) | A collection of OrderInstructionRequests. | [optional] 
## Example

```python
from lusid.models.order_instruction_set_request import OrderInstructionSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[OrderInstructionRequest]] = # Replace with your value
order_instruction_set_request_instance = OrderInstructionSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

