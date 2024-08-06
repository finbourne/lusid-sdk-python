# InstrumentEventHolder

An instrument event equipped with additional metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** | The unique identifier of this corporate action. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The set of identifiers which determine the instrument this event relates to. | 
**lusid_instrument_id** | **str** | The LUID for the instrument. | 
**instrument_scope** | **str** | The scope of the instrument. | 
**description** | **str** | The description of the instrument event. | 
**event_date_range** | [**EventDateRange**](EventDateRange.md) |  | 
**instrument_event** | [**InstrumentEvent**](InstrumentEvent.md) |  | 
**properties** | [**List[PerpetualProperty]**](PerpetualProperty.md) | The properties attached to this instrument event. | [optional] 
**sequence_number** | **int** | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. | [optional] 
**participation_type** | **str** | Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary. | [optional] [default to 'Mandatory']

## Example

```python
from lusid.models.instrument_event_holder import InstrumentEventHolder

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEventHolder from a JSON string
instrument_event_holder_instance = InstrumentEventHolder.from_json(json)
# print the JSON string representation of the object
print InstrumentEventHolder.to_json()

# convert the object into a dict
instrument_event_holder_dict = instrument_event_holder_instance.to_dict()
# create an instance of InstrumentEventHolder from a dict
instrument_event_holder_form_dict = instrument_event_holder.from_dict(instrument_event_holder_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


