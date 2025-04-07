# UpsertInstrumentEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | Free string that uniquely identifies the event within the corporate action source | 
**instrument_identifiers** | **Dict[str, str]** | The set of identifiers which determine the instrument this event relates to. | 
**description** | **str** | The description of the instrument event. | [optional] 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 
**sequence_number** | **int** | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. | [optional] 
**participation_type** | **str** | Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary. | [optional] [default to 'Mandatory']
**event_date_stamps** | [**Dict[str, YearMonthDay]**](YearMonthDay.md) | The date stamps corresponding to the relevant date-time fields for the instrument event. The key for each provided date stamp must match the field name of a valid datetime field from the InstrumentEvent DTO. | [optional] 

## Example

```python
from lusid.models.upsert_instrument_event_request import UpsertInstrumentEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInstrumentEventRequest from a JSON string
upsert_instrument_event_request_instance = UpsertInstrumentEventRequest.from_json(json)
# print the JSON string representation of the object
print UpsertInstrumentEventRequest.to_json()

# convert the object into a dict
upsert_instrument_event_request_dict = upsert_instrument_event_request_instance.to_dict()
# create an instance of UpsertInstrumentEventRequest from a dict
upsert_instrument_event_request_form_dict = upsert_instrument_event_request.from_dict(upsert_instrument_event_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


