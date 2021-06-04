# InstrumentDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instrument. | 
**identifiers** | [**dict(str, InstrumentIdValue)**](InstrumentIdValue.md) | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 
**look_through_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


