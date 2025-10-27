# BlockSetRequest

A request to create or update multiple Blocks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BlockRequest]**](BlockRequest.md) | A collection of BlockRequests. | [optional] 
## Example

```python
from lusid.models.block_set_request import BlockSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[BlockRequest]] = # Replace with your value
block_set_request_instance = BlockSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

