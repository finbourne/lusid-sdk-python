# AllocationEventReallocateRequest

The request used to recompute an unbooked Allocation Event: why, and with which basis values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the event is being recomputed. | 
**basis_values** | [**List[AllocationMapBasisValue]**](AllocationMapBasisValue.md) | Optional replacement basis values per investor record. | [optional] 
## Example

```python
from lusid.models.allocation_event_reallocate_request import AllocationEventReallocateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reason: StrictStr = "example_reason"
basis_values: Optional[List[AllocationMapBasisValue]] = # Replace with your value
allocation_event_reallocate_request_instance = AllocationEventReallocateRequest(reason=reason, basis_values=basis_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

