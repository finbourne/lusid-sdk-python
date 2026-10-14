# CarryAccrualResult

The outcome of a carry accrual: the movement in each partner's carry against what was last accrued.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**period_end** | **datetime** | The date carry is accrued to. | 
**source** | **str** | The waterfall or model the carry amounts came from. | 
**lines** | [**List[CarryAccrualLine]**](CarryAccrualLine.md) | The accrual movement per partner. | 
**booked_transaction_ids** | **List[str]** | The identifiers of the transactions booked, if any. | 
## Example

```python
from lusid.models.carry_accrual_result import CarryAccrualResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
period_end: datetime = # Replace with your value
source: StrictStr = "example_source"
lines: List[CarryAccrualLine] = # Replace with your value
booked_transaction_ids: List[StrictStr] = # Replace with your value
carry_accrual_result_instance = CarryAccrualResult(fund_id=fund_id, period_end=period_end, source=source, lines=lines, booked_transaction_ids=booked_transaction_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

