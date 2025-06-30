# CancelOrderAndMoveRemainingResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_order** | [**Order**](Order.md) |  | [optional] 
**new_order** | [**Order**](Order.md) |  | [optional] 
**new_block_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.cancel_order_and_move_remaining_result import CancelOrderAndMoveRemainingResult
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

cancelled_order: Optional[Order] = # Replace with your value
new_order: Optional[Order] = # Replace with your value
new_block_id: Optional[ResourceId] = # Replace with your value
cancel_order_and_move_remaining_result_instance = CancelOrderAndMoveRemainingResult(cancelled_order=cancelled_order, new_order=new_order, new_block_id=new_block_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

