# InstrumentDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. The name of the instrument | 
**identifiers** | **dict(str, str)** | Required. A set of identifiers that uniquely identify this instrument (e.g FIGI, RIC) | 
**properties** | [**list[InstrumentProperty]**](InstrumentProperty.md) | Optional. A collection of properties to upsert on the instrument. | [optional] 
**look_through_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**InstrumentEconomicDefinition**](InstrumentEconomicDefinition.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


