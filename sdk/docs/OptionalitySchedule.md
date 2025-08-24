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
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, validator

exercise_type: Optional[StrictStr] = "example_exercise_type"
option_entries: Optional[conlist(OptionEntry)] = # Replace with your value
option_type: Optional[StrictStr] = "example_option_type"
schedule_type: StrictStr = "example_schedule_type"
optionality_schedule_instance = OptionalitySchedule(exercise_type=exercise_type, option_entries=option_entries, option_type=option_type, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

