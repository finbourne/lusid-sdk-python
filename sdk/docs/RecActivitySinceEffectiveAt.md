# RecActivitySinceEffectiveAt

A per-side exclusive lower bound on an activity window's effective range.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **datetime** | The exclusive lower bound for the left side. Activity effective at exactly this datetime falls outside the window. | 
**right** | **datetime** | The exclusive lower bound for the right side. Activity effective at exactly this datetime falls outside the window. | 
## Example

```python
from lusid.models.rec_activity_since_effective_at import RecActivitySinceEffectiveAt
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: datetime = # Replace with your value
right: datetime = # Replace with your value
rec_activity_since_effective_at_instance = RecActivitySinceEffectiveAt(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

