# BlockAndOrdersCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockAndOrdersRequest]**](BlockAndOrdersRequest.md) | A collection of BlockAndOrdersRequest. | 
## Example

```python
from lusid.models.block_and_orders_create_request import BlockAndOrdersCreateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: List[BlockAndOrdersRequest] = # Replace with your value
block_and_orders_create_request_instance = BlockAndOrdersCreateRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

