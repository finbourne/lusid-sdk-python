# AllocationServiceRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 
## Example

```python
from lusid.models.allocation_service_run_response import AllocationServiceRunResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, conlist

values: Optional[conlist(ResourceId)] = None
failed: Optional[Dict[str, ErrorDetail]] = None
allocation_service_run_response_instance = AllocationServiceRunResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

