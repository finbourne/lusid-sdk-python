# InstrumentEventHolder

An instrument event equipped with additional metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | The unique identifier of this corporate action. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **dict(str, str)** | The set of identifiers which determine the instrument this event relates to. | 
**lusid_instrument_id** | **str** | The LUID for the instrument. | 
**instrument_scope** | **str** | The scope of the instrument. | 
**description** | **str** | The description of the instrument event. | 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


