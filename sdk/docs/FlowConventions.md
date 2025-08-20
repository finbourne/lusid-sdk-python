# FlowConventions

A flow convention defines the specification for generation of the date schedule for a leg or set of cashflows. It determines the tenor of these and, how to map the unadjusted set of dates to dates which are 'good business days'. For example, if an unadjusted date falls on a Saturday or a bank holiday, should it be rolled forward or backward to obtain the adjusted date. For more information, see https://support.lusid.com/knowledgebase/article/KA-02055/
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the flow convention. | 
**payment_frequency** | **str** | When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is, the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment.  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year and difference between them. For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)              Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**roll_convention** | **str** | For backward compatibility, this can either specify a business day convention or a roll convention. If the business day convention is provided using the BusinessDayConvention property, this must be a valid roll convention.              When used as a roll convention: The conventions specifying the rule used to generate dates in a schedule.  Supported string (enumeration) values are: [None, EndOfMonth, IMM, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, FirstMonday, FirstTuesday, FirstWednesday, FirstThursday, FirstFriday, SecondMonday, SecondTuesday, SecondWednesday, SecondThursday, SecondFriday, ThirdMonday, ThirdTuesday, ThirdWednesday, ThirdThursday, ThirdFriday, FourthMonday, FourthTuesday, FourthWednesday, FourthThursday, FourthFriday, LastMonday, LastTuesday, LastWednesday, LastThursday, LastFriday].              When in backward compatible mode: Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing]. | 
**payment_calendars** | **List[str]** | An array of strings denoting holiday calendars that apply to generation of payment schedules. | 
**reset_calendars** | **List[str]** | An array of strings denoting holiday calendars that apply to generation of reset schedules. | 
**settle_days** | **int** | DEPRECATED Number of Good Business Days between the trade date and the effective or settlement date of the instrument. This field is now deprecated and not picked up in schedule generation or adjustment to bond accrual start date. Defaulted to 0 if not set. | [optional] 
**reset_days** | **int** | The number of Good Business Days between determination and payment of reset. Defaulted to 0 if not set. | [optional] 
**leap_days_included** | **bool** | If this flag is set to true, the 29th of February is included in the date schedule when the business roll convention is applied. If this flag is set to false, the business roll convention ignores February 29 for date schedules, cash flow payments etc. This flag defaults to true if not specified, i.e., leap days are included in a date schedule generation. | [optional] 
**accrual_date_adjustment** | **str** | Indicates if the accrual dates are adjusted using the business day convention. The default value is &#39;Adjusted&#39;.  Supported string (enumeration) values are: [Adjusted, Unadjusted]. | [optional] 
**business_day_convention** | **str** | When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | [optional] 
**accrual_day_count_convention** | **str** | Optional, if not set the main DayCountConvention is used for all accrual calculations. This only needs to be set when accrual uses a different day count to the coupon calculation. | [optional] 
**coupon_payment_lag** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | [optional] 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 
## Example

```python
from lusid.models.flow_conventions import FlowConventions
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, constr, validator

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
leap_days_included: Optional[StrictBool] = # Replace with your value
leap_days_included:Optional[StrictBool] = None
accrual_date_adjustment: Optional[StrictStr] = "example_accrual_date_adjustment"
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
accrual_day_count_convention: Optional[StrictStr] = "example_accrual_day_count_convention"
coupon_payment_lag: Optional[RelativeDateOffset] = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
flow_conventions_instance = FlowConventions(currency=currency, payment_frequency=payment_frequency, day_count_convention=day_count_convention, roll_convention=roll_convention, payment_calendars=payment_calendars, reset_calendars=reset_calendars, settle_days=settle_days, reset_days=reset_days, leap_days_included=leap_days_included, accrual_date_adjustment=accrual_date_adjustment, business_day_convention=business_day_convention, accrual_day_count_convention=accrual_day_count_convention, coupon_payment_lag=coupon_payment_lag, scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

