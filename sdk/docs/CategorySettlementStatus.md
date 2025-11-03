# CategorySettlementStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The Status of the settlement category - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;. | 
**is_overdue** | **bool** | Whether the category has any overdue movements | 
**problems** | [**List[SettlementProblem]**](SettlementProblem.md) | Instruction level detail of rejected or invalid settlement instructions | 
## Example

```python
from lusid.models.category_settlement_status import CategorySettlementStatus
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
is_overdue: StrictBool = # Replace with your value
is_overdue:StrictBool = True
problems: List[SettlementProblem] = # Replace with your value
category_settlement_status_instance = CategorySettlementStatus(status=status, is_overdue=is_overdue, problems=problems)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

