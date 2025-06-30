# HoldingIdsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_ids** | **List[int]** | The array of unique holding identifiers | 
## Example

```python
from lusid.models.holding_ids_request import HoldingIdsRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictInt, conlist

holding_ids: conlist(StrictInt, min_items=1) = Field(..., alias="holdingIds", description="The array of unique holding identifiers")
holding_ids_request_instance = HoldingIdsRequest(holding_ids=holding_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

