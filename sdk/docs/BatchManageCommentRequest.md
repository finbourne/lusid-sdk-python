# BatchManageCommentRequest

One item of a batch comment request. The operation (add/edit/delete) is inferred from the  combination of commentId and commentText.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_result_id** | **str** | The rec result the comment operation targets. | 
**comment_id** | **str** | The comment id. Null with text &#x3D; add; provided with text &#x3D; edit; provided with null text &#x3D; delete. | [optional] 
**comment_text** | **str** | The comment body. See operation inference. | [optional] 
## Example

```python
from lusid.models.batch_manage_comment_request import BatchManageCommentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_result_id: StrictStr = "example_rec_result_id"
comment_id: Optional[StrictStr] = "example_comment_id"
comment_text: Optional[StrictStr] = "example_comment_text"
batch_manage_comment_request_instance = BatchManageCommentRequest(rec_result_id=rec_result_id, comment_id=comment_id, comment_text=comment_text)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

