# SweepBlocksRequest

A request to sweep specified blocks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_ids** | [**List[ResourceId]**](ResourceId.md) | The identifiers of the blocks to sweep. | 
**latest_allowable_modification_time** | **str** | Timestamp, cut label or tenor. A block can only be swept if none of its executions or allocations were modified after this time. A tenor is relative to the current time, for example &#39;1D&#39; means one day ago. A business day tenor, for example &#39;1BD&#39;, requires calendarId. A tenor cannot go back further than 1 January 1900. For more information on tenors, see [Specifying tenors in LUSID](https://support.lusid.com/docs/specifying-tenors-in-lusid) | 
**calendar_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.sweep_blocks_request import SweepBlocksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

block_ids: List[ResourceId] = # Replace with your value
latest_allowable_modification_time: StrictStr = "example_latest_allowable_modification_time"
calendar_id: Optional[ResourceId] = # Replace with your value
sweep_blocks_request_instance = SweepBlocksRequest(block_ids=block_ids, latest_allowable_modification_time=latest_allowable_modification_time, calendar_id=calendar_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

