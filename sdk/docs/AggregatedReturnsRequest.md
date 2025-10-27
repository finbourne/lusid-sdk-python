# AggregatedReturnsRequest

The request used in the AggregatedReturns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[PerformanceReturnsMetric]**](PerformanceReturnsMetric.md) | A list of metrics to calculate in the AggregatedReturns. | 
**return_ids** | [**List[ResourceId]**](ResourceId.md) | The Scope and code of the returns. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**composite_method** | **str** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | **str** | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**output_frequency** | **str** | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
**alternative_inception_date** | **str** | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. | [optional] 
**holiday_calendars** | **List[str]** | The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, &#39;CoppClark&#39;. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | [optional] 
**currency** | **str** | Optional - either a string or a property. If provided, the results will be converted to the specified currency | [optional] 
**run_mode** | **str** | The dates the AggregatedReturns output will be calculated: ReturnData/WeekDays/AllDays/MonthEnd. Defaults to ReturnData. | [optional] 
## Example

```python
from lusid.models.aggregated_returns_request import AggregatedReturnsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metrics: List[PerformanceReturnsMetric] = # Replace with your value
return_ids: Optional[List[ResourceId]] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
composite_method: Optional[StrictStr] = "example_composite_method"
period: Optional[StrictStr] = "example_period"
output_frequency: Optional[StrictStr] = "example_output_frequency"
alternative_inception_date: Optional[StrictStr] = "example_alternative_inception_date"
holiday_calendars: Optional[List[StrictStr]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
run_mode: Optional[StrictStr] = "example_run_mode"
aggregated_returns_request_instance = AggregatedReturnsRequest(metrics=metrics, return_ids=return_ids, recipe_id=recipe_id, composite_method=composite_method, period=period, output_frequency=output_frequency, alternative_inception_date=alternative_inception_date, holiday_calendars=holiday_calendars, currency=currency, run_mode=run_mode)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

