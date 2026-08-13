# RecUserComment

A user-authored comment attached to a rec result. Carried forward with the result across runs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | System-generated GUID identifying the comment. Set once on creation. | 
**comment_text** | **str** | The body of the comment. | 
**user_id** | **str** | The author of the comment. | 
**as_at_created** | **datetime** | The asAt time the comment was created. Set once. | 
**as_at_modified** | **datetime** | The asAt time the comment was last modified. Equals asAtCreated until the first edit. | 
## Example

```python
from lusid.models.rec_user_comment import RecUserComment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

comment_id: StrictStr = "example_comment_id"
comment_text: StrictStr = "example_comment_text"
user_id: StrictStr = "example_user_id"
as_at_created: datetime = # Replace with your value
as_at_modified: datetime = # Replace with your value
rec_user_comment_instance = RecUserComment(comment_id=comment_id, comment_text=comment_text, user_id=user_id, as_at_created=as_at_created, as_at_modified=as_at_modified)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

