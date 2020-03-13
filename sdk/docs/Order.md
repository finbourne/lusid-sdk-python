# Order

An Order for a certain quantity of a specific instrument
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument ordered. | 
**quantity** | **int** | The quantity of given instrument ordered. | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


