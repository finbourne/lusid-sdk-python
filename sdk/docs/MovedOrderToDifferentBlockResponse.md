# MovedOrderToDifferentBlockResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_block** | [**Block**](Block.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**source_block_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.moved_order_to_different_block_response import MovedOrderToDifferentBlockResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

destination_block: Optional[Block] = # Replace with your value
order: Optional[Order] = None
source_block_id: Optional[ResourceId] = # Replace with your value
moved_order_to_different_block_response_instance = MovedOrderToDifferentBlockResponse(destination_block=destination_block, order=order, source_block_id=source_block_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

