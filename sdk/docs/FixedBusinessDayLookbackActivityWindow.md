# FixedBusinessDayLookbackActivityWindow

The activity window whose since bound on each side is a set number of business days before that side's  effectiveAt, counted in a time zone against optional holiday calendars, with each side configured on its own.  Stateless, so it is accepted under every effectiveAtProgression.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**RecBusinessDayLookbackSide**](RecBusinessDayLookbackSide.md) |  | 
**right** | [**RecBusinessDayLookbackSide**](RecBusinessDayLookbackSide.md) |  | 
**window_type** | **str** | Polymorphic discriminator. Supported types: Contiguous, FixedPeriodLookback, FixedBusinessDayLookback. Contiguous requires effectiveAtProgression Series; the lookback types are accepted under any progression. Available values: Contiguous, FixedPeriodLookback, FixedBusinessDayLookback, Explicit, ClosedPeriod, ContiguousAsAt. | 
## Example

```python
from lusid.models.fixed_business_day_lookback_activity_window import FixedBusinessDayLookbackActivityWindow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: RecBusinessDayLookbackSide
right: RecBusinessDayLookbackSide
window_type: StrictStr = "example_window_type"
fixed_business_day_lookback_activity_window_instance = FixedBusinessDayLookbackActivityWindow(left=left, right=right, window_type=window_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

