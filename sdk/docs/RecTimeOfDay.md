# RecTimeOfDay

A local time of day to the minute, read in the time zone of the side that names it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** | The hour of the day, 0 to 23. | 
**minutes** | **int** | The minute of the hour, 0 to 59. | 
## Example

```python
from lusid.models.rec_time_of_day import RecTimeOfDay
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

hours: StrictInt = # Replace with your value
hours: StrictInt = 42
minutes: StrictInt = # Replace with your value
minutes: StrictInt = 42
rec_time_of_day_instance = RecTimeOfDay(hours=hours, minutes=minutes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

