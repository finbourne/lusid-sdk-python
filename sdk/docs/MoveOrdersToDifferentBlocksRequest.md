# MoveOrdersToDifferentBlocksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrderIdRequest]**](BlockAndOrderIdRequest.md) | A collection of BlockAndOrderId. | 
## Example

```python
from lusid.models.move_orders_to_different_blocks_request import MoveOrdersToDifferentBlocksRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

requests: conlist(BlockAndOrderIdRequest, max_items=100, min_items=1) = Field(..., description="A collection of BlockAndOrderId.")
move_orders_to_different_blocks_request_instance = MoveOrdersToDifferentBlocksRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

