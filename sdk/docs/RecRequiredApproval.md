# RecRequiredApproval

An approval slot required for a result set, passed through from the rec definition's review configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_code** | **str** | Client-defined identifier for the approval slot (e.g. &#39;Desk&#39;, &#39;Risk&#39;). | 
**description** | **str** | Human-readable label for the approval slot. | [optional] 
**current_user_can_decide** | **bool** | Whether the calling user may decide this approval slot, pre-evaluated at request time. | [optional] 
## Example

```python
from lusid.models.rec_required_approval import RecRequiredApproval
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

approval_code: StrictStr = "example_approval_code"
description: Optional[StrictStr] = "example_description"
current_user_can_decide: Optional[StrictBool] = # Replace with your value
current_user_can_decide:Optional[StrictBool] = None
rec_required_approval_instance = RecRequiredApproval(approval_code=approval_code, description=description, current_user_can_decide=current_user_can_decide)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

