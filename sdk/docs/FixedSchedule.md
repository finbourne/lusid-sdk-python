# FixedSchedule

Schedule for fixed coupon payments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date from which LUSID starts generating the payment schedule. | 
**maturity_date** | **datetime** | Last date of the payment generation schedule. May not necessarily be the maturity date of the underlying instrument (e.g. in case the instrument has multiple payment schedules). | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**coupon_rate** | **float** | Coupon rate given as a fraction. | [optional] 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**ex_dividend_days** | **int** | Optional. Number of calendar days in the ex-dividend period. If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative. If set, this must be a non-negative number. If not set, or set to 0, then there is no ex-dividend period.              NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration. | [optional] 
**notional** | **float** | Scaling factor, the quantity outstanding on which the rate will be paid. | [optional] 
**payment_currency** | **str** | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. | 
**stub_type** | **str** | When a payment schedule doesn&#39;t have regular payment intervals just because of the first and/or last coupons of the schedule, we call those irregular coupons stubs. This configuration specifies what type of stub is used when building the schedule Supported values are: None &#x3D; this is a regular payment schedule with no stubs. DO NOT use it with irregular schedules or you will get incorrect and unexpected behaviour. ShortFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is shorter than the regular payment period. ShortBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is shorter than the regular payment period. LongFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is longer than the regular payment period. LongBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is longer than the regular payment period. Both &#x3D; this is an irregular payment schedule where both the first and the last coupons are irregular, and the length of these periods is calculated based on the first coupon payment date that should have been explicitly set. | [optional] 
**ex_dividend_configuration** | [**ExDividendConfiguration**](ExDividendConfiguration.md) |  | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 
## Example

```python
from lusid.models.fixed_schedule import FixedSchedule
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
flow_conventions: Optional[FlowConventions] = # Replace with your value
coupon_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
convention_name: Optional[FlowConventionName] = # Replace with your value
ex_dividend_days: Optional[StrictInt] = # Replace with your value
ex_dividend_days: Optional[StrictInt] = None
notional: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
payment_currency: StrictStr = "example_payment_currency"
stub_type: Optional[StrictStr] = "example_stub_type"
ex_dividend_configuration: Optional[ExDividendConfiguration] = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
fixed_schedule_instance = FixedSchedule(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, coupon_rate=coupon_rate, convention_name=convention_name, ex_dividend_days=ex_dividend_days, notional=notional, payment_currency=payment_currency, stub_type=stub_type, ex_dividend_configuration=ex_dividend_configuration, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

