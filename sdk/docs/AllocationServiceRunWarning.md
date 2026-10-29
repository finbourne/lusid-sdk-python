# AllocationServiceRunWarning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**code** | **str** | The kind of warning. One of: OffMinimumIncrement (an allocation&#39;s quantity is not a multiple of the  instrument&#39;s minimum increment), SkippedBooked (an allocation was not changed because transactions are  already booked against it), ExecutionNotAllocated (an execution was excluded from the run). | [optional] 
**message** | **str** | A description of the warning and, where known, why it arose. | [optional] 
**allocation_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**execution_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.allocation_service_run_warning import AllocationServiceRunWarning
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

placement_id: Optional[ResourceId] = # Replace with your value
code: Optional[StrictStr] = "example_code"
message: Optional[StrictStr] = "example_message"
allocation_id: Optional[ResourceId] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
execution_id: Optional[ResourceId] = # Replace with your value
allocation_service_run_warning_instance = AllocationServiceRunWarning(placement_id=placement_id, code=code, message=message, allocation_id=allocation_id, portfolio_id=portfolio_id, execution_id=execution_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

