# InlineAggregationRequest

Specification for an inline aggregation request consisting of an aggregation request and an inlined portfolio on which it is to be performed
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AggregationRequest**](AggregationRequest.md) |  | 
**instruments** | [**list[WeightedInstrument]**](WeightedInstrument.md) | The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


