# AllocationEventEqualisationFeeCatchUp

The management fees one admitted partner owes from the first fee date to the close, as an explicit amount.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The admitted partner the fee catch-up is charged to. | 
**amount** | **float** | The fee catch-up in the event currency. Must not be negative. | 
**due_date** | **datetime** | The date the fee would have been due had the partner been admitted at the first close, from which interest on it accrues when charged. | [optional] 
## Example

```python
from lusid.models.allocation_event_equalisation_fee_catch_up import AllocationEventEqualisationFeeCatchUp
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
due_date: Optional[datetime] = # Replace with your value
allocation_event_equalisation_fee_catch_up_instance = AllocationEventEqualisationFeeCatchUp(investor_record_id=investor_record_id, amount=amount, due_date=due_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

