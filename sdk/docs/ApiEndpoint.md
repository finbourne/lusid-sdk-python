# ApiEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** |  | [optional] 
**http_method** | **str** |  | 
**path** | **str** |  | 
**status** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.api_endpoint import ApiEndpoint
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operation: Optional[StrictStr] = "example_operation"
http_method: StrictStr = "example_http_method"
path: StrictStr = "example_path"
status: Optional[StrictStr] = "example_status"
summary: Optional[StrictStr] = "example_summary"
description: Optional[StrictStr] = "example_description"
api_endpoint_instance = ApiEndpoint(operation=operation, http_method=http_method, path=path, status=status, summary=summary, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

