# FeeAccrual

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date for which the fee accrual has been calculated. | 
**code** | **str** | The code of the fee for which the accrual has been calculated. | 
**name** | **str** | The name of the fee for which the accrual has been calculated. | 
**calculation_base** | **float** | The result of the evaluating the fee&#39;s calculation base expression. | [optional] 
**amount** | **float** | The result of applying the fee to the calculation base, and scaled down to a day. | [optional] 
**previous_accrual** | **float** | The previous valuation point&#39;s total accrual. | [optional] 
**previous_total_accrual** | **float** | The previous valuation point&#39;s total accrual. | [optional] 
**total_accrual** | **float** | The sum of the PreviousAccrual and Amount. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee_accrual import FeeAccrual
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist, constr, validator
from datetime import datetime
effective_at: datetime = # Replace with your value
code: StrictStr = "example_code"
name: StrictStr = "example_name"
calculation_base: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_total_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
total_accrual: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[conlist(Link)] = None
fee_accrual_instance = FeeAccrual(effective_at=effective_at, code=code, name=name, calculation_base=calculation_base, amount=amount, previous_accrual=previous_accrual, previous_total_accrual=previous_total_accrual, total_accrual=total_accrual, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

