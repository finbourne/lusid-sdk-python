# RecReview

A summary of the per-result review state across the result set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_reviewed** | **int** | The number of results with review status Reviewed. | 
**count_required** | **int** | The number of results with review status Required. | 
**count_not_required** | **int** | The number of results with review status Not Required. | 
**completion_ratio** | **float** | Reviewed / (Reviewed + Required). Is 1.0 when the denominator is zero, and null when execution failed. | [optional] 
## Example

```python
from lusid.models.rec_review import RecReview
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

count_reviewed: StrictInt = # Replace with your value
count_reviewed: StrictInt = 42
count_required: StrictInt = # Replace with your value
count_required: StrictInt = 42
count_not_required: StrictInt = # Replace with your value
count_not_required: StrictInt = 42
completion_ratio: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rec_review_instance = RecReview(count_reviewed=count_reviewed, count_required=count_required, count_not_required=count_not_required, completion_ratio=completion_ratio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

