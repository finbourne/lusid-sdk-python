# BlockAndOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**orders** | [**List[Order]**](Order.md) |  | 
## Example

```python
from lusid.models.block_and_orders import BlockAndOrders
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

block: Block
orders: List[Order]
block_and_orders_instance = BlockAndOrders(block=block, orders=orders)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

