# Instrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**lusid_instrument_id** | **str** | The lusid instrument id (LUID) of the instrument | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**name** | **str** | The name of the instrument | [optional] 
**identifiers** | **dict(str, str)** | The set of identifiers that can be used to uniquely identify the instrument | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | Any requested instrument properties. If no property can be found for the instrument, then  a value of &#39;Unknown&#39; will be returned | [optional] 
**lookthrough_portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_definition** | [**InstrumentEconomicDefinition**](InstrumentEconomicDefinition.md) |  | [optional] 
**state** | **str** |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


