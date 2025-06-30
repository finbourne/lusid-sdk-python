# BlockAndOrderIdRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_block_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.block_and_order_id_request import BlockAndOrderIdRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

destination_block_id: ResourceId = # Replace with your value
order_id: ResourceId = # Replace with your value
block_and_order_id_request_instance = BlockAndOrderIdRequest(destination_block_id=destination_block_id, order_id=order_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

