# InformationalEvent

A generic event derived from the economic definition of an instrument. This should be considered purely  informational; any data provided by this event is not guaranteed to be processable by LUSID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | What type of internal event does this represent; reset, exercise, amortisation etc. | [readonly] 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**anchor_date** | **datetime** | In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window. | 
**event_window_end** | **datetime** | In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window. | [optional] [readonly] 
**diagnostics** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.informational_event import InformationalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InformationalEvent from a JSON string
informational_event_instance = InformationalEvent.from_json(json)
# print the JSON string representation of the object
print InformationalEvent.to_json()

# convert the object into a dict
informational_event_dict = informational_event_instance.to_dict()
# create an instance of InformationalEvent from a dict
informational_event_form_dict = informational_event.from_dict(informational_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


