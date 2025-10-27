# WorkspaceUpdateRequest

A request to update a workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A friendly description for the workspace. | 
## Example

```python
from lusid.models.workspace_update_request import WorkspaceUpdateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

description: StrictStr = "example_description"
workspace_update_request_instance = WorkspaceUpdateRequest(description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

