# PlaceBlocksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PlacementRequest]**](PlacementRequest.md) | A collection of PlacementRequest. | 
## Example

```python
from lusid.models.place_blocks_request import PlaceBlocksRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

requests: conlist(PlacementRequest, max_items=100, min_items=1) = Field(..., description="A collection of PlacementRequest.")
place_blocks_request_instance = PlaceBlocksRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

