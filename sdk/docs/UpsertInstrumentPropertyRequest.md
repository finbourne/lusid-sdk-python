# UpsertInstrumentPropertyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_type** | **str** | The unique identifier type to search for the instrument, for example &#39;Figi&#39;. | 
**identifier** | **str** | A value of that type to identify the instrument to upsert properties for, for example &#39;BBG000BLNNV0&#39;. | 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | A set of instrument properties and associated values to store for the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


