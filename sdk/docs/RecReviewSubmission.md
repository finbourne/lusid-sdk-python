# RecReviewSubmission

When the reviewer is allowed to submit their work for approval. Omit it to let them submit at any time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_ratio_threshold** | **float** | The review completion ratio a result set has to reach before it can be submitted, between 0.0 and 1.0 inclusive. | 
**auto_submit** | **bool** | Whether the system submits on the reviewer&#39;s behalf as soon as the completion ratio threshold is met, rather than waiting to be asked. | [optional] 
## Example

```python
from lusid.models.rec_review_submission import RecReviewSubmission
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

completion_ratio_threshold: Union[StrictFloat, StrictInt] = # Replace with your value
auto_submit: Optional[StrictBool] = # Replace with your value
auto_submit:Optional[StrictBool] = None
rec_review_submission_instance = RecReviewSubmission(completion_ratio_threshold=completion_ratio_threshold, auto_submit=auto_submit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

