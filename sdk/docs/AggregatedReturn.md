# AggregatedReturn

A list of Aggregated Returns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the return. | 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**metrics_value** | **dict(str, float)** | The value for the specified metric. | 
**frequency** | **str** | Show the aggregated output returns on a Daily or Monthly period. | [optional] 
**composite_members** | **int** | The number of members in the Composite on the given day. | [optional] 
**composite_members_without_return** | [**list[ResourceId]**](ResourceId.md) | List containing Composite members which post no return on the given day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


