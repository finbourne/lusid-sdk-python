# CancelSchedule

Cancel schedule represents the embedded option on a cancellable swap, allowing one party to  terminate the swap on one or more predefined dates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_dates** | **List[datetime]** | The dates on which cancellation may be elected. | 
**cancel_type** | **str** | The type of cancellation option: European (single cancel date) or Bermudan (two or more).                Supported string (enumeration) values are: [European, Bermudan]. Available values: European, Bermudan. | 
**notice_convention** | [**NoticeConvention**](NoticeConvention.md) |  | 
**schedule_type** | **str** | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, Invalid, CancelSchedule. | 
## Example

```python
from lusid.models.cancel_schedule import CancelSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cancel_dates: List[datetime] = # Replace with your value
cancel_type: StrictStr = "example_cancel_type"
notice_convention: NoticeConvention = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
cancel_schedule_instance = CancelSchedule(cancel_dates=cancel_dates, cancel_type=cancel_type, notice_convention=notice_convention, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

