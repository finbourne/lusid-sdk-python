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

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceReturnsMetric from a JSON string
performance_returns_metric_instance = PerformanceReturnsMetric.from_json(json)
# print the JSON string representation of the object
print PerformanceReturnsMetric.to_json()

# convert the object into a dict
performance_returns_metric_dict = performance_returns_metric_instance.to_dict()
# create an instance of PerformanceReturnsMetric from a dict
performance_returns_metric_form_dict = performance_returns_metric.from_dict(performance_returns_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


