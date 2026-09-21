# ContiguousActivityWindow

The activity window for a running series of instances: each instance's window starts where the previous  instance's ended, so the series tiles the effective timeline with no gaps and no overlap. Requires the  definition's effectiveAtProgression to be Series.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_activity_since_effective_at** | [**RecActivitySinceEffectiveAt**](RecActivitySinceEffectiveAt.md) |  | 
**window_type** | **str** | Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt. | 
## Example

```python
from lusid.models.contiguous_activity_window import ContiguousActivityWindow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

initial_activity_since_effective_at: RecActivitySinceEffectiveAt = # Replace with your value
window_type: StrictStr = "example_window_type"
contiguous_activity_window_instance = ContiguousActivityWindow(initial_activity_since_effective_at=initial_activity_since_effective_at, window_type=window_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

