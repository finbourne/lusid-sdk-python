# LusidInstrument

Base class in hierarchy for LUSID Instruments. Valuation would normally be performed through passing LUSID a Code for a portfolio to be valued.  In that case the set of instruments have already been uploaded. Equally, one might wish to pass in a set of instruments directly and have LUSID  value the inlined set. This the base instrument for this case.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | Instrument type, must be property for JSON. | [optional] 
**type** | **str** |  | [default to 'Finbourne.WebApi.Interface.Dto.Instruments.LusidInstrument']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


