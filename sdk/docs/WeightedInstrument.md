# WeightedInstrument

Specification for a holding or quantity of (weight for) an instrument on a given date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | The quantity of the instrument that is owned. | [optional] 
**holding_identifier** | **str** | Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments. | [optional] 
**instrument** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


