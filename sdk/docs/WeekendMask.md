# WeekendMask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | [**List[DayOfWeek]**](DayOfWeek.md) |  | 
**time_zone** | **str** |  | 
## Example

```python
from lusid.models.weekend_mask import WeekendMask
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

days: conlist(str) = # Replace with your value
time_zone: StrictStr = "example_time_zone"
weekend_mask_instance = WeekendMask(days=days, time_zone=time_zone)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

