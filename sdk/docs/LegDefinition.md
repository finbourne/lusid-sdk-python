# LegDefinition

Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**index_convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional_exchange_type** | **str** | what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both]. | 
**pay_receive** | **str** | Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive]. | 
**rate_or_spread** | **float** | Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. | 
**reset_convention** | **str** | Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  Defaults to \&quot;InAdvance\&quot; if not set. | [optional] 
**stub_type** | **str** | If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. | 
**compounding** | [**Compounding**](Compounding.md) |  | [optional] 
**amortisation** | [**StepSchedule**](StepSchedule.md) |  | [optional] 
**first_regular_payment_date** | **datetime** | Optional payment date of the first regular coupon.  Must be greater than the StartDate.  If set, the regular coupon schedule will be built such that the first regular coupon  will end on this date. The start date of this coupon will be calculated as normal and  a stub coupon will be created from the StartDate to the start of the first regular coupon. | [optional] 
**first_coupon_type** | **str** | Optional coupon type setting for the first coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. | [optional] 
**last_regular_payment_date** | **datetime** | Optional payment date of the last regular coupon.  Must be less than the Maturity date.  If set, the regular coupon schedule will be built up to this date and the final  coupon will be a stub between this date and the Maturity date. | [optional] 
**last_coupon_type** | **str** | Optional coupon type setting for the last coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. | [optional] 
**fx_linked_notional_schedule** | [**FxLinkedNotionalSchedule**](FxLinkedNotionalSchedule.md) |  | [optional] 
**intermediate_notional_exchange** | **bool** | Indicates whether there are intermediate notional exchanges. | [optional] 
## Example

```python
from lusid.models.leg_definition import LegDefinition
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
convention_name: Optional[FlowConventionName] = # Replace with your value
conventions: Optional[FlowConventions] = None
index_convention: Optional[IndexConvention] = # Replace with your value
index_convention_name: Optional[FlowConventionName] = # Replace with your value
notional_exchange_type: StrictStr = "example_notional_exchange_type"
pay_receive: StrictStr = "example_pay_receive"
rate_or_spread: Union[StrictFloat, StrictInt] = # Replace with your value
reset_convention: Optional[StrictStr] = "example_reset_convention"
stub_type: StrictStr = "example_stub_type"
compounding: Optional[Compounding] = None
amortisation: Optional[StepSchedule] = None
first_regular_payment_date: Optional[datetime] = # Replace with your value
first_coupon_type: Optional[StrictStr] = "example_first_coupon_type"
last_regular_payment_date: Optional[datetime] = # Replace with your value
last_coupon_type: Optional[StrictStr] = "example_last_coupon_type"
fx_linked_notional_schedule: Optional[FxLinkedNotionalSchedule] = # Replace with your value
intermediate_notional_exchange: Optional[StrictBool] = # Replace with your value
intermediate_notional_exchange:Optional[StrictBool] = None
leg_definition_instance = LegDefinition(convention_name=convention_name, conventions=conventions, index_convention=index_convention, index_convention_name=index_convention_name, notional_exchange_type=notional_exchange_type, pay_receive=pay_receive, rate_or_spread=rate_or_spread, reset_convention=reset_convention, stub_type=stub_type, compounding=compounding, amortisation=amortisation, first_regular_payment_date=first_regular_payment_date, first_coupon_type=first_coupon_type, last_regular_payment_date=last_regular_payment_date, last_coupon_type=last_coupon_type, fx_linked_notional_schedule=fx_linked_notional_schedule, intermediate_notional_exchange=intermediate_notional_exchange)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

