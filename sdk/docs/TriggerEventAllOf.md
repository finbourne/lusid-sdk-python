# TriggerEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | The underlying price level that triggers the event | 
**trigger_type** | **str** | The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch | 
**trigger_direction** | **str** | The direction of the trigger; valid options are Up and Down | 
**trigger_date** | **datetime** | The date the trigger happens at. | 
**maturity_date** | **datetime** | The date the trigger takes effect. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.trigger_event_all_of import TriggerEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerEventAllOf from a JSON string
trigger_event_all_of_instance = TriggerEventAllOf.from_json(json)
# print the JSON string representation of the object
print TriggerEventAllOf.to_json()

# convert the object into a dict
trigger_event_all_of_dict = trigger_event_all_of_instance.to_dict()
# create an instance of TriggerEventAllOf from a dict
trigger_event_all_of_form_dict = trigger_event_all_of.from_dict(trigger_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


