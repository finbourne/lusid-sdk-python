# CarryAccrualLine

One partner's line on a carry accrual.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the amount belongs to. | 
**previous_carry_to_date** | **float** | The cumulative carry already on the books for the partner. | 
**carry_to_date** | **float** | The cumulative carry the partner has earned to the period end. | 
**delta** | **float** | The accrual booked: the carry to date less what was already on the books. | 
**clawback_exposure** | **float** | The carry that would have to be returned if the fund liquidated at the period end. | 
**status** | **str** | What happened to the line. Available values: Unchanged, Accrued, Released. | 
## Example

```python
from lusid.models.carry_accrual_line import CarryAccrualLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
previous_carry_to_date: Union[StrictFloat, StrictInt] = # Replace with your value
carry_to_date: Union[StrictFloat, StrictInt] = # Replace with your value
delta: Union[StrictFloat, StrictInt] = # Replace with your value
clawback_exposure: Union[StrictFloat, StrictInt] = # Replace with your value
status: StrictStr = "example_status"
carry_accrual_line_instance = CarryAccrualLine(investor_record_id=investor_record_id, previous_carry_to_date=previous_carry_to_date, carry_to_date=carry_to_date, delta=delta, clawback_exposure=clawback_exposure, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

