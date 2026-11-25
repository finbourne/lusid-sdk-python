# RecBusinessDayLookbackSide

One side of a FixedBusinessDayLookback activity window: how many business days the side reaches back, the time  zone the days are counted in, the holiday calendars that take days out of the count, and the local time the  since bound falls at.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookback_business_days** | **int** | The number of business days before the effectiveAt&#39;s local date the window opens on, from 1 to 366. If the effectiveAt falls on a non-business day it counts from the most recent business day before it. | 
**time_zone** | **str** | The IANA time zone (e.g. Europe/London, Asia/Hong_Kong) the effectiveAt is read in and the business days are counted in. The since bound is stamped in UTC. | 
**holiday_calendars** | [**List[ResourceId]**](ResourceId.md) | Up to 5 holiday calendars whose dates are not business days, each by scope and code. A day that is a weekend or a holiday in any of them is skipped. With none, business days are Monday to Friday. Every calendar must exist when the definition is written and when a rec is instantiated. | [optional] 
**since_time_of_day** | [**RecTimeOfDay**](RecTimeOfDay.md) |  | [optional] 
## Example

```python
from lusid.models.rec_business_day_lookback_side import RecBusinessDayLookbackSide
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lookback_business_days: StrictInt = # Replace with your value
lookback_business_days: StrictInt = 42
time_zone: StrictStr = "example_time_zone"
holiday_calendars: Optional[List[ResourceId]] = # Replace with your value
since_time_of_day: Optional[RecTimeOfDay] = # Replace with your value
rec_business_day_lookback_side_instance = RecBusinessDayLookbackSide(lookback_business_days=lookback_business_days, time_zone=time_zone, holiday_calendars=holiday_calendars, since_time_of_day=since_time_of_day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

