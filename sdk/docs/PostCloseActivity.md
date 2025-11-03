# PostCloseActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | 
**entity_unique_id** | **str** |  | 
**as_at** | **datetime** |  | 
**effective_at** | **str** |  | [optional] 
## Example

```python
from lusid.models.post_close_activity import PostCloseActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_unique_id: StrictStr = "example_entity_unique_id"
as_at: datetime = # Replace with your value
effective_at: Optional[StrictStr] = "example_effective_at"
post_close_activity_instance = PostCloseActivity(entity_type=entity_type, entity_unique_id=entity_unique_id, as_at=as_at, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

