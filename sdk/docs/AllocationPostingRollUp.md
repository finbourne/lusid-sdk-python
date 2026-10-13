# AllocationPostingRollUp

One roll-up a booking writes on a vehicle's line on the register above it, summing the lines beneath.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side. | [optional] 
**line** | **str** | The roll-up line, rendered as the held vehicle and the register above it. | [optional] 
**portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**amount** | **float** | The amount posted, in the event currency. | [optional] 
**component** | **str** | The component of the event the posting carries. | [optional] 
**sum_of** | **List[str]** | The identifiers of the postings beneath that the roll-up sums. | [optional] 
## Example

```python
from lusid.models.allocation_posting_roll_up import AllocationPostingRollUp
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
line: Optional[StrictStr] = "example_line"
portfolio: Optional[ResourceId] = None
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
component: Optional[StrictStr] = "example_component"
sum_of: Optional[List[StrictStr]] = # Replace with your value
allocation_posting_roll_up_instance = AllocationPostingRollUp(id=id, line=line, portfolio=portfolio, amount=amount, component=component, sum_of=sum_of)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

