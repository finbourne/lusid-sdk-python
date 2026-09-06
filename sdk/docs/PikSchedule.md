# PikSchedule

A PikSchedule represents Payment-in-Kind features for a ComplexBond.  It works in conjunction with existing FixedSchedules or FloatSchedules to define  how interest is paid during duration of the schedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the PIK schedule period. | 
**maturity_date** | **datetime** | The end date of the PIK schedule period. | 
**is_pik_fraction_electable** | **bool** | If true, the PIK fraction is electable at each payment date.  Defaults to false. | [optional] 
**pik_fraction** | **float** | The fraction of the coupon that is paid in kind, where 0 means fully cash and 1 means fully PIK.  Required if IsPikFractionElectable is false or null. Must satisfy 0 &lt;&#x3D; pikFraction &lt;&#x3D; 1. | [optional] 
**pik_margin** | **float** | The portion of the coupon that is paid in kind, stated in the leg&#39;s own rate units (an annualised  rate on the notional) rather than as a fraction of the coupon. The in-kind leg accrues at this flat  rate and the cash leg accrues the remainder of the coupon, so on a floating leg the in-kind portion  stays constant across fixings — the shape of a loan quoted as \&quot;index + 700bp, of which 250bp paid  in kind\&quot;. On a fixed leg it is equivalent to pikFraction &#x3D; pikMargin / couponRate. Should the  period&#39;s whole coupon fall below the margin, the in-kind portion is capped at the whole  (non-negative) coupon and the cash leg floors at zero.  Mutually exclusive with pikFraction, pikRate, pikSpread and isPikFractionElectable.  Must be greater than or equal to zero. null indicates the split is stated by pikFraction instead. | [optional] 
**pik_payment_type** | **str** | The type of PIK payment to be used for the duration of this schedule.  InterestCapitalisation adds the paid-in-kind portion to the bond&#39;s current face;  AdditionalSecurities settles it by delivering units of another instrument, named on each  period&#39;s PikBondInterestEvent; Electable leaves the choice to a per-period election.                Supported string (enumeration) values are: [Electable, InterestCapitalisation, AdditionalSecurities]. | [optional] 
**pik_rate** | **float** | The PIK interest rate. Must be greater than or equal to zero.  null indicates no override PIK interest rate. | [optional] 
**pik_spread** | **float** | The PIK spread to be added to the base rate for the final PIK rate.  null indicates no spread on base rate. | [optional] 
**schedule_type** | **str** | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule. | 
## Example

```python
from lusid.models.pik_schedule import PikSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
is_pik_fraction_electable: Optional[StrictBool] = # Replace with your value
is_pik_fraction_electable:Optional[StrictBool] = None
pik_fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pik_margin: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pik_payment_type: Optional[StrictStr] = "example_pik_payment_type"
pik_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pik_spread: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
pik_schedule_instance = PikSchedule(start_date=start_date, maturity_date=maturity_date, is_pik_fraction_electable=is_pik_fraction_electable, pik_fraction=pik_fraction, pik_margin=pik_margin, pik_payment_type=pik_payment_type, pik_rate=pik_rate, pik_spread=pik_spread, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

