# ResetEvent

Definition of a reset event.  This is an event that describes a reset or fixing for an instrument such as the floating payment on  a swap cash flow.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The quantity associated with the reset. This will only be populated if the information is known. | [optional] 
**reset_type** | **str** | The type of the reset; e.g. RIC, Currency-pair | 
**fixing_source** | **str** | Fixing identification source, if available. | [optional] 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**fixing_date** | **datetime** | The date the reset fixes, or is observed upon. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.reset_event import ResetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResetEvent from a JSON string
reset_event_instance = ResetEvent.from_json(json)
# print the JSON string representation of the object
print ResetEvent.to_json()

# convert the object into a dict
reset_event_dict = reset_event_instance.to_dict()
# create an instance of ResetEvent from a dict
reset_event_form_dict = reset_event.from_dict(reset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


