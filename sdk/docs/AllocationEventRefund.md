# AllocationEventRefund

Cash the fund owes back to an investor record.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the refund is owed to. | [optional] 
**amount** | **float** | The amount owed back, in the event currency. | [optional] 
**reason** | **str** | Why the refund arose: Overpayment or Reversal. | [optional] 
## Example

```python
from lusid.models.allocation_event_refund import AllocationEventRefund
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
allocation_event_refund_instance = AllocationEventRefund(investor_record_id=investor_record_id, amount=amount, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

