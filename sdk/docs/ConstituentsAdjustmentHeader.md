# ConstituentsAdjustmentHeader

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | There can be at most one holdings adjustment for a portfolio at a  specific effective time so this uniquely identifies the adjustment. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.constituents_adjustment_header import ConstituentsAdjustmentHeader
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
effective_at: Optional[datetime] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
constituents_adjustment_header_instance = ConstituentsAdjustmentHeader(effective_at=effective_at, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

