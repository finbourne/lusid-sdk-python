# SweepBlocksRequest

A request to sweep specified blocks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_ids** | [**Dict[str, ResourceId]**](ResourceId.md) | A dictionary mapping ephemeral identifiers, which live as long as the request, to specific blocks to sweep. | 
**latest_allowable_modification_time** | **str** | Timestamp or cut label which the  block or related entities must not have been updated after. | 
## Example

```python
from lusid.models.sweep_blocks_request import SweepBlocksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

block_ids: Dict[str, ResourceId] = # Replace with your value
latest_allowable_modification_time: StrictStr = "example_latest_allowable_modification_time"
sweep_blocks_request_instance = SweepBlocksRequest(block_ids=block_ids, latest_allowable_modification_time=latest_allowable_modification_time)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

