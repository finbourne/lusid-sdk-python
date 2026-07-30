# RecSubmission

An entry in the append-only log of review submissions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user who submitted the review. | 
**comment_text** | **str** | An optional comment from the submitter. | [optional] 
**as_at_submitted** | **datetime** | The asAt datetime at which the submission was made. | 
**as_at_superseded** | **datetime** | The asAt datetime at which this entry was superseded. Null when it is the current standing entry. | [optional] 
## Example

```python
from lusid.models.rec_submission import RecSubmission
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

user_id: StrictStr = "example_user_id"
comment_text: Optional[StrictStr] = "example_comment_text"
as_at_submitted: datetime = # Replace with your value
as_at_superseded: Optional[datetime] = # Replace with your value
rec_submission_instance = RecSubmission(user_id=user_id, comment_text=comment_text, as_at_submitted=as_at_submitted, as_at_superseded=as_at_superseded)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

