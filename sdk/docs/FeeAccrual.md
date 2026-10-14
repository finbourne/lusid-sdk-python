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
links: Optional[List[Link]] = None
fee_accrual_instance = FeeAccrual(effective_at=effective_at, code=code, name=name, calculation_base=calculation_base, amount=amount, previous_accrual=previous_accrual, previous_total_accrual=previous_total_accrual, total_accrual=total_accrual, cap_period_accrual=cap_period_accrual, fee_cap_applied=fee_cap_applied, fee_floor_applied=fee_floor_applied, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

