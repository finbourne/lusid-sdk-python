# SubmitRecResultSetReviewRequest

The request to submit a result set review for approval (or resubmit after addressing revisions).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_text** | **str** | An optional comment recorded on the submission. | [optional] 
## Example

```python
from lusid.models.submit_rec_result_set_review_request import SubmitRecResultSetReviewRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

comment_text: Optional[StrictStr] = "example_comment_text"
submit_rec_result_set_review_request_instance = SubmitRecResultSetReviewRequest(comment_text=comment_text)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

