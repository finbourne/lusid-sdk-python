# LatestAsAt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.latest_as_at import LatestAsAt
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
links: Optional[List[Link]] = None
latest_as_at_instance = LatestAsAt(as_at=as_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

