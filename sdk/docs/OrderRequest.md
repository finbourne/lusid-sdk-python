# OrderRequest

A request to create or update an Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument ordered. | 
**quantity** | **int** | The quantity of given instrument ordered. | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**code** | **str** | Uniquely identifies this order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


