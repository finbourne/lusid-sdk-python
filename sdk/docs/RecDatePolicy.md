# RecDatePolicy

The date policy of a rec definition: how the effective dates of successive instances may progress, whether each  side reconciles at the latest knowledge or at a pinned asAt, and — for activity-based rec types — how the  activity window is bounded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at_progression** | **str** | How the effective dates of successive instances may progress. Series (the default): each instance&#39;s leftEffectiveAt and rightEffectiveAt must be strictly after the previous instance&#39;s. Unconstrained: no relationship between instances. Immutable once the definition has instances. Available values: Series, Unconstrained. | [optional] 
**as_at_policy** | [**RecAsAtPolicy**](RecAsAtPolicy.md) |  | [optional] 
**activity_window** | [**RecActivityWindow**](RecActivityWindow.md) |  | [optional] 
## Example

```python
from lusid.models.rec_date_policy import RecDatePolicy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at_progression: Optional[StrictStr] = "example_effective_at_progression"
as_at_policy: Optional[RecAsAtPolicy] = # Replace with your value
activity_window: Optional[RecActivityWindow] = # Replace with your value
rec_date_policy_instance = RecDatePolicy(effective_at_progression=effective_at_progression, as_at_policy=as_at_policy, activity_window=activity_window)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

