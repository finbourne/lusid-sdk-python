# OptionalitySchedule

Optionality Schedule represents a class for creation of schedules for optionality (call, put)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exercise_type** | **str** | The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American]. | [optional] 
**option_entries** | [**List[OptionEntry]**](OptionEntry.md) | The dates at which the bond call/put may be actioned, and associated strikes. | [optional] 
**option_type** | **str** | Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put]. | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 

## Example

```python
from lusid.models.optionality_schedule import OptionalitySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of OptionalitySchedule from a JSON string
optionality_schedule_instance = OptionalitySchedule.from_json(json)
# print the JSON string representation of the object
print OptionalitySchedule.to_json()

# convert the object into a dict
optionality_schedule_dict = optionality_schedule_instance.to_dict()
# create an instance of OptionalitySchedule from a dict
optionality_schedule_form_dict = optionality_schedule.from_dict(optionality_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


