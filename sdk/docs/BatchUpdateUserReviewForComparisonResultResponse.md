# BatchUpdateUserReviewForComparisonResultResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, GroupReconciliationComparisonResult]**](GroupReconciliationComparisonResult.md) | The collection of comparison results that have been successfully updated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The collection of comparison results that could not be updated with the provided user input along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Contains warnings related to the updated comparison result user input | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_update_user_review_for_comparison_result_response import BatchUpdateUserReviewForComparisonResultResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, GroupReconciliationComparisonResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
batch_update_user_review_for_comparison_result_response_instance = BatchUpdateUserReviewForComparisonResultResponse(values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

