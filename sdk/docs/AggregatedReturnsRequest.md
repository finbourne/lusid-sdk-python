# AggregatedReturnsRequest

The request used in the AggregatedReturns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**list[PerformanceReturnsMetric]**](PerformanceReturnsMetric.md) | A list of metrics to calculate in the AggregatedReturns. | 
**return_ids** | [**list[ResourceId]**](ResourceId.md) | The Scope and code of the returns. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**composite_method** | **str** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | **str** | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**output_frequency** | **str** | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
**alternative_inception_date** | **str** | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


