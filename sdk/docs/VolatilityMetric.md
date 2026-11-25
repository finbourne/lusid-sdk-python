# VolatilityMetric

The volatility of the returns over a window looking back from each period of the grid: the population  standard deviation of the period returns in the window (divided by the number of returns, not one fewer).  It is measured over business days. Calculated returns have a return for every calendar day, so the return  of a day that is not a business day is linked into the next business day: those of the business calendar  of the Returns entity, or every day but Saturdays and Sundays when it has none. Such a day reports the  volatility of the business day before it. A window over a count of returns therefore counts business days  for a volatility, and calendar days for the other metrics. Upserted returns are measured as they were  upserted. When the window asks for it to be annualised, the volatility is scaled by the square root of  252, a year of business days.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | [**ReturnsMetricWindow**](ReturnsMetricWindow.md) |  | 
**type** | **str** | Available values: Return, IndicativeAmount, Volatility. | 
**alias** | **str** |  | [optional] 
## Example

```python
from lusid.models.volatility_metric import VolatilityMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

window: ReturnsMetricWindow
type: StrictStr = "example_type"
alias: Optional[StrictStr] = "example_alias"
volatility_metric_instance = VolatilityMetric(window=window, type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

