# StepSchedule

Schedule that steps at known dated points in time.  Used in representation of a sinking bond, also called amortisation, steps in coupons for fixed bonds and spreads for floating bonds.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_type** | **str** | The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage]. | 
**step_schedule_type** | **str** | The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread]. | 
**steps** | [**List[LevelStep]**](LevelStep.md) | The level steps which are applied. | 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 

## Example

```python
from lusid.models.step_schedule import StepSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of StepSchedule from a JSON string
step_schedule_instance = StepSchedule.from_json(json)
# print the JSON string representation of the object
print StepSchedule.to_json()

# convert the object into a dict
step_schedule_dict = step_schedule_instance.to_dict()
# create an instance of StepSchedule from a dict
step_schedule_form_dict = step_schedule.from_dict(step_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


