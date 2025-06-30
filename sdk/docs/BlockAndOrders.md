# BlockAndOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**orders** | [**List[Order]**](Order.md) |  | 
## Example

```python
from lusid.models.block_and_orders import BlockAndOrders
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

block: Block = # Replace with your value
orders: conlist(Order) = # Replace with your value
block_and_orders_instance = BlockAndOrders(block=block, orders=orders)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

