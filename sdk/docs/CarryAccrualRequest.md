# CarryAccrualRequest

The request to accrue carried interest on a partnership fund from amounts a waterfall has produced.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_end** | **datetime** | The date carry is accrued to. | 
**source** | **str** | The waterfall or model the carry amounts came from. | 
**amounts** | [**List[CarryAccrualAmount]**](CarryAccrualAmount.md) | The carry each partner has earned to the period end, as the source states it. | 
**book** | **bool** | When true, the accrual deltas are booked. | [optional] 
## Example

```python
from lusid.models.carry_accrual_request import CarryAccrualRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_end: datetime = # Replace with your value
source: StrictStr = "example_source"
amounts: List[CarryAccrualAmount] = # Replace with your value
book: Optional[StrictBool] = # Replace with your value
book:Optional[StrictBool] = None
carry_accrual_request_instance = CarryAccrualRequest(period_end=period_end, source=source, amounts=amounts, book=book)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

