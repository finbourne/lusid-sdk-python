# PerformanceReturnsMetric

The request used in the AggregatedReturns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the metric. Default to Return | [optional] 
**window** | **str** | The given metric for the calculation i.e. 1Y, 1D. | [optional] 
**allow_partial** | **bool** | Bool if the metric is allowed partial results. Deafult to false. | [optional] 
**annualised** | **bool** | Bool if the metric is annualized. Default to false. | [optional] 
**with_fee** | **bool** | Bool if the metric should consider the fees when is calculated. Default to false. | [optional] 
**seed_amount** | **float** | The given seed amount for the calculation of the indicative amount metrics. | [optional] 
**alias** | **str** | The alias for the metric. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


