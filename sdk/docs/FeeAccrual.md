# FeeAccrual

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date for which the fee accrual has been calculated. | 
**code** | **str** | The code of the fee for which the accrual has been calculated. | 
**name** | **str** | The name of the fee for which the accrual has been calculated. | 
**calculation_base** | **float** | The basis the annual accrual derives from: the result of evaluating the fee&#39;s calculation base expression, or the configured annual amount for a fixed-amount fee. | [optional] 
**amount** | **float** | The result of applying the fee to the calculation base, and scaled down to a day. | [optional] 
**previous_accrual** | **float** | The previous valuation point&#39;s total accrual. | [optional] 
**previous_total_accrual** | **float** | The previous valuation point&#39;s total accrual. | [optional] 
**total_accrual** | **float** | The sum of the PreviousAccrual and Amount. | [optional] 
**cap_period_accrual** | **float** | The amount accrued so far in the current fee year (from the fee&#39;s AnchorDate), in the fund currency, against which an annual FeeCap is assessed. | [optional] 
**fee_cap_applied** | **bool** | Whether the FeeCap reduced the amount accrued at this valuation point. | [optional] 
**fee_floor_applied** | **bool** | Whether the FeeFloor raised the amount accrued at this valuation point. | [optional] 
**is_payable_date** | **bool** | Whether the valuation point&#39;s window, from the day after the previous valuation point to this one, holds one of the fee&#39;s payable dates, set by its PayableFrequency and AnchorDate and rolled by its BusinessDayConvention. | [optional] 
**payable_date** | **datetime** | The latest payable date of the fee in the valuation point&#39;s window, after business day adjustment. Null when the window holds no payable date. | [optional] 
**payable_amount** | **float** | The accrued balance that became payable at this valuation point: the previous valuation point&#39;s AccruedBalance plus the accrual through the end of the PayableDate, less what the fund&#39;s own transactions tagged with the fee&#39;s code in a Transaction/&lt;fund scope&gt;/FeeCode property deemed payable on or before it. Several payable dates in one window give one combined payable. Never negative: zero when the window holds no payable date, or when the balance due is not positive, as when tagged transactions already deemed more than was due. A share class&#39;s PayableAmount is its share of the fund&#39;s, apportioned by each class&#39;s balance due before deems, so the classes&#39; add up to the fund&#39;s. | [optional] 
**accrued_balance** | **float** | The amount accrued and not yet payable. It resets on a payable date, unlike TotalAccrual, and the total consideration of each of the fund&#39;s transactions in the valuation point&#39;s window tagged with the fee&#39;s code in a Transaction/&lt;fund scope&gt;/FeeCode property comes off it. A negative balance, from deeming more than was due, nets off later accruals before anything is payable again, as a prepaid fee does. | [optional] 
**previous_accrued_balance** | **float** | The previous valuation point&#39;s AccruedBalance. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee_accrual import FeeAccrual
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: datetime = # Replace with your value
code: StrictStr = "example_code"
name: StrictStr = "example_name"
calculation_base: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_total_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
total_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cap_period_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fee_cap_applied: Optional[StrictBool] = # Replace with your value
fee_cap_applied:Optional[StrictBool] = None
fee_floor_applied: Optional[StrictBool] = # Replace with your value
fee_floor_applied:Optional[StrictBool] = None
is_payable_date: Optional[StrictBool] = # Replace with your value
is_payable_date:Optional[StrictBool] = None
payable_date: Optional[datetime] = # Replace with your value
payable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accrued_balance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_accrued_balance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
fee_accrual_instance = FeeAccrual(effective_at=effective_at, code=code, name=name, calculation_base=calculation_base, amount=amount, previous_accrual=previous_accrual, previous_total_accrual=previous_total_accrual, total_accrual=total_accrual, cap_period_accrual=cap_period_accrual, fee_cap_applied=fee_cap_applied, fee_floor_applied=fee_floor_applied, is_payable_date=is_payable_date, payable_date=payable_date, payable_amount=payable_amount, accrued_balance=accrued_balance, previous_accrued_balance=previous_accrued_balance, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

