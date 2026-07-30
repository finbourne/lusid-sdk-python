# RecResultCountByReviewStatus

Result counts broken down by review status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **int** | The number of results with review status Required. | 
**not_required** | **int** | The number of results with review status Not Required. | 
**reviewed** | **int** | The number of results with review status Reviewed. | 
## Example

```python
from lusid.models.rec_result_count_by_review_status import RecResultCountByReviewStatus
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

required: StrictInt = # Replace with your value
required: StrictInt = 42
not_required: StrictInt = # Replace with your value
not_required: StrictInt = 42
reviewed: StrictInt = # Replace with your value
reviewed: StrictInt = 42
rec_result_count_by_review_status_instance = RecResultCountByReviewStatus(required=required, not_required=not_required, reviewed=reviewed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

