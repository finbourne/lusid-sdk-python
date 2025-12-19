# FundValuationSchedule

Specification object for the valuation schedule, how do we determine which days we wish to perform a valuation upon.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **str** | If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range. | [optional] 
**effective_at** | **str** | The market data time, i.e. the time to run the valuation request effective of. | [optional] 
**diary_entry** | **str** | The diary entry to use for the valuation schedule. This is used to determine the date on which the valuation should be performed. | [optional] 
**variant** | **str** | The diary entry variant to use, together with the diary entry to be used for the valuation schedule. | [optional] 
**tenor** | **str** | Tenor, e.g \&quot;1D\&quot;, \&quot;1M\&quot; to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same. | [optional] 
**roll_convention** | **str** | When Tenor is given and is \&quot;1M\&quot; or longer, this specifies the rule which should be used to generate the date schedule.  For example, \&quot;EndOfMonth\&quot; to generate end of month dates, or \&quot;1\&quot; to specify the first day of the applicable month. | [optional] 
**holiday_calendars** | **List[str]** | The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \&quot;CoppClark\&quot;.  Note that when the calendars are not available (e.g. when the user has insufficient permissions),  a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | [optional] 
**valuation_date_times** | **List[str]** | If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given. | [optional] 
**business_day_convention** | **str** | When Tenor is given and is not equal to \&quot;1D\&quot;, there may be cases where \&quot;date + tenor\&quot; land on non-business days around month end.  In that case, the BusinessDayConvention, e.g. modified following \&quot;MF\&quot; would be applied to determine the next GBD. | [optional] 
## Example

```python
from lusid.models.fund_valuation_schedule import FundValuationSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_from: Optional[StrictStr] = "example_effective_from"
effective_at: Optional[StrictStr] = "example_effective_at"
diary_entry: Optional[StrictStr] = "example_diary_entry"
variant: Optional[StrictStr] = "example_variant"
tenor: Optional[StrictStr] = "example_tenor"
roll_convention: Optional[StrictStr] = "example_roll_convention"
holiday_calendars: Optional[List[StrictStr]] = # Replace with your value
valuation_date_times: Optional[List[StrictStr]] = # Replace with your value
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
fund_valuation_schedule_instance = FundValuationSchedule(effective_from=effective_from, effective_at=effective_at, diary_entry=diary_entry, variant=variant, tenor=tenor, roll_convention=roll_convention, holiday_calendars=holiday_calendars, valuation_date_times=valuation_date_times, business_day_convention=business_day_convention)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

