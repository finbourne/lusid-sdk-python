# ProcessingGroupSchedule

Specification of the dates on which a Processing Group is executed: a date range plus  tenor / roll / business-day conventions and holiday calendars that generate the schedule,  or an explicit override set of dates. Modelled on the valuation schedule shape, without the  bitemporal timeline fields.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **str** | The start of the date range over which the schedule is generated. | [optional] 
**effective_at** | **str** | The end of the date range over which the schedule is generated. | [optional] 
**tenor** | **str** | Tenor, e.g. \&quot;1D\&quot;, \&quot;1M\&quot;, used to generate the date schedule between EffectiveFrom and EffectiveAt. | [optional] 
**roll_convention** | **str** | When Tenor is \&quot;1M\&quot; or longer, the rule used to generate the date schedule, e.g. \&quot;EndOfMonth\&quot; or \&quot;1\&quot;. | [optional] 
**holiday_calendars** | **List[str]** | The holiday calendar(s), by name, used when determining business days for the schedule. | [optional] 
**schedule_dates** | **List[str]** | If given, the exact set of dates on which to execute. Overrides the generated schedule. | [optional] 
**business_day_convention** | **str** | When Tenor is not \&quot;1D\&quot;, the convention (e.g. \&quot;MF\&quot;) used to roll dates that land on non-business days. | [optional] 
**time_zone** | **str** | The IANA approved time zone (tzdb id, e.g. \&quot;Europe/London\&quot;) the schedule is expressed in.  Informational for consumers of the schedule: the generated schedule dates are calendar dates  and are not adjusted by this time zone. Optional. | [optional] 
**business_day_offset** | **int** | If given, the number of good business days (per the holiday calendars) added to each generated  date. Can be negative. For example, the 10th business day of each month is a \&quot;1M\&quot; tenor with an  \&quot;EndOfMonth\&quot; roll convention and a business day offset of 10. Cannot be combined with ScheduleDates. | [optional] 
**date_exceptions** | **List[str]** | Dates, in yyyy-MM-dd format, on which the Processing Group does not run. These are removed  from the generated schedule after all other conventions and offsets have been applied. | [optional] 
## Example

```python
from lusid.models.processing_group_schedule import ProcessingGroupSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_from: Optional[StrictStr] = "example_effective_from"
effective_at: Optional[StrictStr] = "example_effective_at"
tenor: Optional[StrictStr] = "example_tenor"
roll_convention: Optional[StrictStr] = "example_roll_convention"
holiday_calendars: Optional[List[StrictStr]] = # Replace with your value
schedule_dates: Optional[List[StrictStr]] = # Replace with your value
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
time_zone: Optional[StrictStr] = "example_time_zone"
business_day_offset: Optional[StrictInt] = # Replace with your value
business_day_offset: Optional[StrictInt] = None
date_exceptions: Optional[List[StrictStr]] = # Replace with your value
processing_group_schedule_instance = ProcessingGroupSchedule(effective_from=effective_from, effective_at=effective_at, tenor=tenor, roll_convention=roll_convention, holiday_calendars=holiday_calendars, schedule_dates=schedule_dates, business_day_convention=business_day_convention, time_zone=time_zone, business_day_offset=business_day_offset, date_exceptions=date_exceptions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

