# InstrumentPaymentDiaryRow

An individual row containing details of a single cashflow in the diary.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. | [optional] 
**currency** | **str** | The payment currency of the cash flow. | [optional] 
**payment_date** | **datetime** | The date at which the given cash flow is due to be paid. | [optional] 
**pay_or_receive** | **str** | Does the cash flow belong to the Pay or Receive leg. | [optional] 
**accrual_start** | **datetime** | The date on which accruals start for this cashflow. | [optional] 
**accrual_end** | **datetime** | The date on which accruals end for this cashflow. | [optional] 
**cash_flow_type** | **str** | The type of cashflow. | [optional] 
**is_cash_flow_determined** | **bool** | Is the cashflow determined as of the effective date time. | [optional] 
**is_cash_flow_historic** | **bool** | Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt. | [optional] 
**discount_factor** | **float** | Weighting factor to discount cashflow to the present value. | [optional] 
**discounted_expected_cash_flow_amount** | **float** | The expected cashflow amount taking into account the discount factor. | [optional] 
**day_count_fraction** | **float** | The day count fraction, if appropriate. | [optional] 
**forward_rate** | **float** | Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg) | [optional] 
**reset_rate** | **float** | The value of the reset, if any. | [optional] 
**spread** | **float** | The spread that exists on the payoff. | [optional] 
## Example

```python
from lusid.models.instrument_payment_diary_row import InstrumentPaymentDiaryRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
payment_date: Optional[datetime] = # Replace with your value
pay_or_receive: Optional[StrictStr] = "example_pay_or_receive"
accrual_start: Optional[datetime] = # Replace with your value
accrual_end: Optional[datetime] = # Replace with your value
cash_flow_type: Optional[StrictStr] = "example_cash_flow_type"
is_cash_flow_determined: Optional[StrictBool] = # Replace with your value
is_cash_flow_determined:Optional[StrictBool] = None
is_cash_flow_historic: Optional[StrictBool] = # Replace with your value
is_cash_flow_historic:Optional[StrictBool] = None
discount_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
discounted_expected_cash_flow_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
day_count_fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
forward_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reset_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
spread: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_payment_diary_row_instance = InstrumentPaymentDiaryRow(quantity=quantity, currency=currency, payment_date=payment_date, pay_or_receive=pay_or_receive, accrual_start=accrual_start, accrual_end=accrual_end, cash_flow_type=cash_flow_type, is_cash_flow_determined=is_cash_flow_determined, is_cash_flow_historic=is_cash_flow_historic, discount_factor=discount_factor, discounted_expected_cash_flow_amount=discounted_expected_cash_flow_amount, day_count_fraction=day_count_fraction, forward_rate=forward_rate, reset_rate=reset_rate, spread=spread)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

