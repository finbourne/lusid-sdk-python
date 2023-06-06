# StepScheduleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_type** | **str** | The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage]. | 
**step_schedule_type** | **str** | The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread]. | 
**steps** | [**List[LevelStep]**](LevelStep.md) | The level steps which are applied. | 
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid | 

## Example

```python
from lusid.models.step_schedule_all_of import StepScheduleAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of StepScheduleAllOf from a JSON string
step_schedule_all_of_instance = StepScheduleAllOf.from_json(json)
# print the JSON string representation of the object
print StepScheduleAllOf.to_json()

# convert the object into a dict
step_schedule_all_of_dict = step_schedule_all_of_instance.to_dict()
# create an instance of StepScheduleAllOf from a dict
step_schedule_all_of_form_dict = step_schedule_all_of.from_dict(step_schedule_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


