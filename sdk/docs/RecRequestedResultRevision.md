# RecRequestedResultRevision

A result flagged for re-review as part of a Request Revisions decision.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_result_id** | **str** | The identifier of the result to flag for re-review. | 
**comment_text** | **str** | An optional per-result comment added to the result&#39;s user comments. | [optional] 
## Example

```python
from lusid.models.rec_requested_result_revision import RecRequestedResultRevision
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_result_id: StrictStr = "example_rec_result_id"
comment_text: Optional[StrictStr] = "example_comment_text"
rec_requested_result_revision_instance = RecRequestedResultRevision(rec_result_id=rec_result_id, comment_text=comment_text)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

