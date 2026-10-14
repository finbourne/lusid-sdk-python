# CarryAccrualAmount

A partner's carry to date as produced by the waterfall.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the amount belongs to. | 
**carry_to_date** | **float** | The cumulative carry the partner has earned to the period end. | 
**by_tier** | [**List[CarryTierAmount]**](CarryTierAmount.md) | The carry by waterfall tier. | [optional] 
**clawback_exposure** | **float** | The carry that would have to be returned if the fund liquidated at the period end. | [optional] 
## Example

```python
from lusid.models.carry_accrual_amount import CarryAccrualAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
carry_to_date: Union[StrictFloat, StrictInt] = # Replace with your value
by_tier: Optional[List[CarryTierAmount]] = # Replace with your value
clawback_exposure: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
carry_accrual_amount_instance = CarryAccrualAmount(investor_record_id=investor_record_id, carry_to_date=carry_to_date, by_tier=by_tier, clawback_exposure=clawback_exposure)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

