# OrderSetRequest

A request to create or update multiple Orders.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_requests** | [**List[OrderRequest]**](OrderRequest.md) | A collection of OrderRequests. | [optional] 
## Example

```python
from lusid.models.order_set_request import OrderSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_requests: Optional[List[OrderRequest]] = # Replace with your value
order_set_request_instance = OrderSetRequest(order_requests=order_requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

