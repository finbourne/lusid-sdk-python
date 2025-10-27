# PlacementSetRequest

A request to create or update multiple Placements.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PlacementRequest]**](PlacementRequest.md) | A collection of PlacementRequests. | [optional] 
## Example

```python
from lusid.models.placement_set_request import PlacementSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[PlacementRequest]] = # Replace with your value
placement_set_request_instance = PlacementSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

