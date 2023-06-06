# ExerciseEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**LusidInstrument**](LusidInstrument.md) |  | 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**anchor_date** | **datetime** | The date the exercise window starts, or point it takes effect on. | 
**event_window_end** | **datetime** | The date the exercise window ends, or point it takes effect on. | [optional] [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.exercise_event_all_of import ExerciseEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ExerciseEventAllOf from a JSON string
exercise_event_all_of_instance = ExerciseEventAllOf.from_json(json)
# print the JSON string representation of the object
print ExerciseEventAllOf.to_json()

# convert the object into a dict
exercise_event_all_of_dict = exercise_event_all_of_instance.to_dict()
# create an instance of ExerciseEventAllOf from a dict
exercise_event_all_of_form_dict = exercise_event_all_of.from_dict(exercise_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


