# UpsertInstrumentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**values** | [**dict(str, Instrument)**](Instrument.md) | The collection of upserted instruments with their latest parameters. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | If any instruments failed to be upserted, they will be listed in &#39;Failed&#39;, along  with a reason why. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


