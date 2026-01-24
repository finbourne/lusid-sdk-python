# PostCloseActivitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_close_activities** | [**List[PostCloseActivity]**](PostCloseActivity.md) | A collection of post-close activities. | 
## Example

```python
from lusid.models.post_close_activities_request import PostCloseActivitiesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

post_close_activities: List[PostCloseActivity] = # Replace with your value
post_close_activities_request_instance = PostCloseActivitiesRequest(post_close_activities=post_close_activities)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

