# AllocationServiceRunAllocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**allocation** | [**Allocation**](Allocation.md) |  | [optional] 
**outcome** | **str** | What the run did to this allocation. One of: Created (by this run), Updated (an existing allocation  whose fields changed), Unchanged (an existing allocation the run left as it was), Cancelled (moved to a  cancelled state or reduced to zero quantity), Skipped (left alone because transactions are already booked  against it; see the SkippedBooked warning). | [optional] 
## Example

```python
from lusid.models.allocation_service_run_allocation import AllocationServiceRunAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

placement_id: Optional[ResourceId] = # Replace with your value
allocation: Optional[Allocation] = None
outcome: Optional[StrictStr] = "example_outcome"
allocation_service_run_allocation_instance = AllocationServiceRunAllocation(placement_id=placement_id, allocation=allocation, outcome=outcome)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

