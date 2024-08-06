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

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedReturnsRequest from a JSON string
aggregated_returns_request_instance = AggregatedReturnsRequest.from_json(json)
# print the JSON string representation of the object
print AggregatedReturnsRequest.to_json()

# convert the object into a dict
aggregated_returns_request_dict = aggregated_returns_request_instance.to_dict()
# create an instance of AggregatedReturnsRequest from a dict
aggregated_returns_request_form_dict = aggregated_returns_request.from_dict(aggregated_returns_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


