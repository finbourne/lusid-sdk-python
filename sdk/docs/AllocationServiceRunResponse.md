# AllocationServiceRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) | The placements that were allocated successfully. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The placements that could not be allocated, keyed by placement, with the reason. | [optional] 
**allocations** | [**List[AllocationServiceRunAllocation]**](AllocationServiceRunAllocation.md) | Every allocation the run touched across the successful placements, each with its outcome. | [optional] 
**warnings** | [**List[AllocationServiceRunWarning]**](AllocationServiceRunWarning.md) | Warnings raised while allocating the successful placements. | [optional] 
## Example

```python
from lusid.models.allocation_service_run_response import AllocationServiceRunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[List[ResourceId]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
allocations: Optional[List[AllocationServiceRunAllocation]] = # Replace with your value
warnings: Optional[List[AllocationServiceRunWarning]] = # Replace with your value
allocation_service_run_response_instance = AllocationServiceRunResponse(values=values, failed=failed, allocations=allocations, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

