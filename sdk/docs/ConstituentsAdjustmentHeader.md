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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: Optional[datetime] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
constituents_adjustment_header_instance = ConstituentsAdjustmentHeader(effective_at=effective_at, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

