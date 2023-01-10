# UpsertInstrumentEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | Free string that uniquely identifies the event within the corporate action source | 
**instrument_identifiers** | **dict(str, str)** | The set of identifiers which determine the instrument this event relates to. | 
**description** | **str** | The description of the instrument event. | [optional] 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**list[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


