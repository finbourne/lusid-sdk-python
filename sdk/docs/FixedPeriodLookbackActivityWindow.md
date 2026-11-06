# FixedPeriodLookbackActivityWindow

The activity window whose since bound on each side is that side's effectiveAt less a fixed ISO 8601 period,  the same period on both sides. Stateless, so it is accepted under every effectiveAtProgression.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookback_period** | **str** | The ISO 8601 period each side&#39;s window reaches back from its effectiveAt, e.g. P1D or PT12H. Whole counts of years, months, days, hours, minutes and seconds (P[n]Y[n]M[n]DT[n]H[n]M[n]S); weeks and fractions are not supported. Must be greater than zero, and applies to both sides. Evaluated in UTC, so P1D is exactly 24 hours. The since bound is exclusive. | 
**window_type** | **str** | Polymorphic discriminator. Supported types: Contiguous, FixedPeriodLookback. Contiguous requires effectiveAtProgression Series; FixedPeriodLookback is accepted under any progression. Available values: Contiguous, FixedPeriodLookback, Explicit, ClosedPeriod, ContiguousAsAt. | 
## Example

```python
from lusid.models.fixed_period_lookback_activity_window import FixedPeriodLookbackActivityWindow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lookback_period: StrictStr = "example_lookback_period"
window_type: StrictStr = "example_window_type"
fixed_period_lookback_activity_window_instance = FixedPeriodLookbackActivityWindow(lookback_period=lookback_period, window_type=window_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

