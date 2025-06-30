# OrderSetRequest

A request to create or update multiple Orders.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_requests** | [**List[OrderRequest]**](OrderRequest.md) | A collection of OrderRequests. | [optional] 
## Example

```python
from lusid.models.order_set_request import OrderSetRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

order_requests: Optional[conlist(OrderRequest)] = # Replace with your value
order_set_request_instance = OrderSetRequest(order_requests=order_requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

