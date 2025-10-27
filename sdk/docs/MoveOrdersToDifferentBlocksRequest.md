# MoveOrdersToDifferentBlocksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrderIdRequest]**](BlockAndOrderIdRequest.md) | A collection of BlockAndOrderId. | 
## Example

```python
from lusid.models.move_orders_to_different_blocks_request import MoveOrdersToDifferentBlocksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: List[BlockAndOrderIdRequest] = # Replace with your value
move_orders_to_different_blocks_request_instance = MoveOrdersToDifferentBlocksRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

