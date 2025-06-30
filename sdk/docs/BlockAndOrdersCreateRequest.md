# BlockAndOrdersCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrdersRequest]**](BlockAndOrdersRequest.md) | A collection of BlockAndOrdersRequest. | 
## Example

```python
from lusid.models.block_and_orders_create_request import BlockAndOrdersCreateRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

requests: conlist(BlockAndOrdersRequest, max_items=100, min_items=1) = Field(..., description="A collection of BlockAndOrdersRequest.")
block_and_orders_create_request_instance = BlockAndOrdersCreateRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

