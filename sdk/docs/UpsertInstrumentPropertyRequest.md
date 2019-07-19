# UpsertInstrumentPropertyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** | The unique Lusid Instrument Identifier (LUID) of the instrument to update or insert properties on. | 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 
**deleted_properties** | [**list[DeleteInstrumentPropertyRequest]**](DeleteInstrumentPropertyRequest.md) | Set of unique instrument properties to delete from the instrument. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


