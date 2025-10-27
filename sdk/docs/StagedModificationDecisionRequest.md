# StagedModificationDecisionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. | 
**comment** | **str** | Comment on decision. | 
## Example

```python
from lusid.models.staged_modification_decision_request import StagedModificationDecisionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

decision: StrictStr = "example_decision"
comment: StrictStr = "example_comment"
staged_modification_decision_request_instance = StagedModificationDecisionRequest(decision=decision, comment=comment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

