# RecReviewRequiredApproval

One approval a submitted review has to collect, and who may give it. All of a configuration's approvals are  required, they may be given in any order, and no user may give more than one of them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | The client-defined identifier for the approval, e.g. \&quot;Desk\&quot; or \&quot;Risk\&quot;. Each may appear at most once. | 
**description** | **str** | A human-readable label for the approval. | [optional] 
**deciding_user** | **str** | A boolean expression over the user attempting the approval, which has to hold for them to give it. They must also hold the entitlement for the decide action. | [optional] 
## Example

```python
from lusid.models.rec_review_required_approval import RecReviewRequiredApproval
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

approval_code: StrictStr = "example_approval_code"
description: Optional[StrictStr] = "example_description"
deciding_user: Optional[StrictStr] = "example_deciding_user"
rec_review_required_approval_instance = RecReviewRequiredApproval(approval_code=approval_code, description=description, deciding_user=deciding_user)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

