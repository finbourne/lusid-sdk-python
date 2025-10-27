# PlaceBlocksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PlacementRequest]**](PlacementRequest.md) | A collection of PlacementRequest. | 
## Example

```python
from lusid.models.place_blocks_request import PlaceBlocksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: List[PlacementRequest] = # Replace with your value
place_blocks_request_instance = PlaceBlocksRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

