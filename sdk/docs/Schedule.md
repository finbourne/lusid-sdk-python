# Schedule

Base class for representing schedules in LUSID.  This base class should not be directly instantiated; each supported ScheduleType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid | 

## Example

```python
from lusid.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print Schedule.to_json()

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_form_dict = schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


