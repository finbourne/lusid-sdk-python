# ExecutionSetRequest

A request to create or update multiple Executions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ExecutionRequest]**](ExecutionRequest.md) | A collection of ExecutionRequests. | [optional] 
## Example

```python
from lusid.models.execution_set_request import ExecutionSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[ExecutionRequest]] = # Replace with your value
execution_set_request_instance = ExecutionSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

