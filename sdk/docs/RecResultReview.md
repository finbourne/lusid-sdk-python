# RecResultReview

The per-result review axis: the workflow state and the recorded review decision. Always present,  including on Match and Cross.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The review workflow state: NotRequired, Required or Reviewed. Available values: NotRequired, Required, Reviewed. | 
**decision** | **str** | The recorded review decision. Null until a decision is made. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate. | [optional] 
**decision_group** | [**RecResultDecisionGroup**](RecResultDecisionGroup.md) |  | [optional] 
## Example

```python
from lusid.models.rec_result_review import RecResultReview
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
decision: Optional[StrictStr] = "example_decision"
decision_group: Optional[RecResultDecisionGroup] = # Replace with your value
rec_result_review_instance = RecResultReview(status=status, decision=decision, decision_group=decision_group)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

