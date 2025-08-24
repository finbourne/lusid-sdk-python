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
from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, constr, validator

level_type: StrictStr = "example_level_type"
step_schedule_type: StrictStr = "example_step_schedule_type"
steps: conlist(LevelStep) = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
step_schedule_instance = StepSchedule(level_type=level_type, step_schedule_type=step_schedule_type, steps=steps, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

