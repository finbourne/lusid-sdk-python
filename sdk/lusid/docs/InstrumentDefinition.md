# InstrumentDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. The name of the instrument | 
**identifiers** | [**dict(str, InstrumentIdValue)**](InstrumentIdValue.md) | Required. A set of identifiers that identify this instrument (BBG123456)  with the key being the type of identifier (RIC, FIGI).  Must include atleast one unique identifier. | 
**properties** | [**list[InstrumentProperty]**](InstrumentProperty.md) | Optional. A collection of properties to upsert on the instrument. | [optional] 
**look_through_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**InstrumentEconomicDefinition**](InstrumentEconomicDefinition.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


