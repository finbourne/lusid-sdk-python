# Instrument

A list of instruments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**scope** | **str** | The scope in which the instrument lies. | [optional] 
**lusid_instrument_id** | **str** | The unique LUSID Instrument Identifier (LUID) of the instrument. | 
**version** | [**Version**](Version.md) |  | 
**name** | **str** | The name of the instrument. | 
**identifiers** | **dict(str, str)** | The set of identifiers that can be used to identify the instrument. | 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | The requested instrument properties. These will be from the &#39;Instrument&#39; domain. | [optional] 
**lookthrough_portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**state** | **str** | The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive | 
**asset_class** | **str** | The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | [optional] 
**dom_ccy** | **str** | The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


