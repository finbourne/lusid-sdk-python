# CancelOrdersAndMoveRemainingRequest

A request to create or update a Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_order_id** | [**ResourceId**](ResourceId.md) |  | 
**move_remaining_to_order_id** | [**ResourceId**](ResourceId.md) |  | 
**move_remaining_to_block_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.cancel_orders_and_move_remaining_request import CancelOrdersAndMoveRemainingRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cancel_order_id: ResourceId = # Replace with your value
move_remaining_to_order_id: ResourceId = # Replace with your value
move_remaining_to_block_id: ResourceId = # Replace with your value
cancel_orders_and_move_remaining_request_instance = CancelOrdersAndMoveRemainingRequest(cancel_order_id=cancel_order_id, move_remaining_to_order_id=move_remaining_to_order_id, move_remaining_to_block_id=move_remaining_to_block_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

