# BatchReviewRecResultRequest

One item of a batch review request: applies review content to its targeted rec result(s). Exactly  one target, except FixAsGroup/ForceMatch which require two or more.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_result_ids** | **List[str]** | The rec results targeted by this batch item. Exactly one, except FixAsGroup/ForceMatch which require two or more. | 
**decision** | [**RecResultDecisionUpdate**](RecResultDecisionUpdate.md) |  | [optional] 
**assigned_user** | [**RecResultAssignmentUpdate**](RecResultAssignmentUpdate.md) |  | [optional] 
**assigned_role** | [**RecResultAssignmentUpdate**](RecResultAssignmentUpdate.md) |  | [optional] 
**add_comment_text** | **str** | Optional comment text to add to each targeted result. | [optional] 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) | Properties in the RecResult domain. Filterable and sortable. | [optional] 
## Example

```python
from lusid.models.batch_review_rec_result_request import BatchReviewRecResultRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_result_ids: List[StrictStr] = # Replace with your value
decision: Optional[RecResultDecisionUpdate] = None
assigned_user: Optional[RecResultAssignmentUpdate] = # Replace with your value
assigned_role: Optional[RecResultAssignmentUpdate] = # Replace with your value
add_comment_text: Optional[StrictStr] = "example_add_comment_text"
properties: Optional[List[PerpetualProperty]] = # Replace with your value
batch_review_rec_result_request_instance = BatchReviewRecResultRequest(rec_result_ids=rec_result_ids, decision=decision, assigned_user=assigned_user, assigned_role=assigned_role, add_comment_text=add_comment_text, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

