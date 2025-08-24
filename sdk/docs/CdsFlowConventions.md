# CdsFlowConventions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roll_frequency** | **str** | The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | [optional] 
**currency** | **str** | Currency of the flow convention. | 
**payment_frequency** | **str** | When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment. | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**roll_convention** | **str** | For backward compatibility, this can either specify a business day convention or a roll convention. If the business  day convention is provided using the BusinessDayConvention property, this must be a valid roll convention.                When used as a roll convention:  The conventions specifying the rule used to generate dates in a schedule.    Supported string (enumeration) values are: [None, EndOfMonth, IMM, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, FirstMonday, FirstTuesday, FirstWednesday, FirstThursday, FirstFriday, SecondMonday, SecondTuesday, SecondWednesday, SecondThursday, SecondFriday, ThirdMonday, ThirdTuesday, ThirdWednesday, ThirdThursday, ThirdFriday, FourthMonday, FourthTuesday, FourthWednesday, FourthThursday, FourthFriday, LastMonday, LastTuesday, LastWednesday, LastThursday, LastFriday].                When in backward compatible mode:  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing]. | 
**payment_calendars** | **List[str]** | An array of strings denoting holiday calendars that apply to generation of payment schedules. | 
**reset_calendars** | **List[str]** | An array of strings denoting holiday calendars that apply to generation of reset schedules. | 
**settle_days** | **int** | Number of Good Business Days between the trade date and the effective or settlement date of the instrument. Defaults to 0 if not set. | [optional] 
**reset_days** | **int** | The number of Good Business Days between determination and payment of reset. Defaults to 0 if not set. | [optional] 
**business_day_convention** | **str** | When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.    Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | [optional] 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 
## Example

```python
from lusid.models.cds_flow_conventions import CdsFlowConventions
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator

roll_frequency: Optional[StrictStr] = "example_roll_frequency"
currency: StrictStr = "example_currency"
payment_frequency: StrictStr = "example_payment_frequency"
day_count_convention: StrictStr = "example_day_count_convention"
roll_convention: StrictStr = "example_roll_convention"
payment_calendars: conlist(StrictStr) = # Replace with your value
reset_calendars: conlist(StrictStr) = # Replace with your value
settle_days: Optional[StrictInt] = # Replace with your value
settle_days: Optional[StrictInt] = None
reset_days: Optional[StrictInt] = # Replace with your value
reset_days: Optional[StrictInt] = None
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
cds_flow_conventions_instance = CdsFlowConventions(roll_frequency=roll_frequency, currency=currency, payment_frequency=payment_frequency, day_count_convention=day_count_convention, roll_convention=roll_convention, payment_calendars=payment_calendars, reset_calendars=reset_calendars, settle_days=settle_days, reset_days=reset_days, business_day_convention=business_day_convention, scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

