# PostCloseActivitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_close_activities** | [**List[PostCloseActivity]**](PostCloseActivity.md) | Collection of post close activites. | 
## Example

```python
from lusid.models.post_close_activities_request import PostCloseActivitiesRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

post_close_activities: conlist(PostCloseActivity) = # Replace with your value
post_close_activities_request_instance = PostCloseActivitiesRequest(post_close_activities=post_close_activities)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

