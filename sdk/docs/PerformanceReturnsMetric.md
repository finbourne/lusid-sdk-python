# PerformanceReturnsMetric

The request used in the AggregatedReturns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the metric. Default to Return | [optional] 
**window** | **str** | The given metric for the calculation i.e. 1Y, 1D. | [optional] 
**allow_partial** | **bool** | Bool if the metric is allowed partial results. Default to false. | [optional] 
**annualised** | **bool** | Bool if the metric is annualized. Default to false. | [optional] 
**with_fee** | **bool** | Bool if the metric should consider the fees when is calculated. Default to false. | [optional] 
**seed_amount** | **str** | The given seed amount for the calculation of the indicative amount metrics. | [optional] 
**alias** | **str** | The alias for the metric. | [optional] 
## Example

```python
from lusid.models.performance_returns_metric import PerformanceReturnsMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
window: Optional[StrictStr] = "example_window"
allow_partial: Optional[StrictBool] = # Replace with your value
allow_partial:Optional[StrictBool] = None
annualised: Optional[StrictBool] = # Replace with your value
annualised:Optional[StrictBool] = None
with_fee: Optional[StrictBool] = # Replace with your value
with_fee:Optional[StrictBool] = None
seed_amount: Optional[StrictStr] = "example_seed_amount"
alias: Optional[StrictStr] = "example_alias"
performance_returns_metric_instance = PerformanceReturnsMetric(type=type, window=window, allow_partial=allow_partial, annualised=annualised, with_fee=with_fee, seed_amount=seed_amount, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

