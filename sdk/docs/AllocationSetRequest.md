# AllocationSetRequest

A request to create or update multiple Allocations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_requests** | [**List[AllocationRequest]**](AllocationRequest.md) | A collection of AllocationRequests. | [optional] 
## Example

```python
from lusid.models.allocation_set_request import AllocationSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allocation_requests: Optional[List[AllocationRequest]] = # Replace with your value
allocation_set_request_instance = AllocationSetRequest(allocation_requests=allocation_requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

