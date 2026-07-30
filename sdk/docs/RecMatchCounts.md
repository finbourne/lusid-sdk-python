# RecMatchCounts

Counts for non-exception results (Match, Cross).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of results in this category. | 
**by_result_type** | [**RecMatchCountByResultType**](RecMatchCountByResultType.md) |  | 
**by_review_status** | [**RecResultCountByReviewStatus**](RecResultCountByReviewStatus.md) |  | 
## Example

```python
from lusid.models.rec_match_counts import RecMatchCounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

total: StrictInt = # Replace with your value
total: StrictInt = 42
by_result_type: RecMatchCountByResultType = # Replace with your value
by_review_status: RecResultCountByReviewStatus = # Replace with your value
rec_match_counts_instance = RecMatchCounts(total=total, by_result_type=by_result_type, by_review_status=by_review_status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

