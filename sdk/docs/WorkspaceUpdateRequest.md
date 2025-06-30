# WorkspaceUpdateRequest

A request to update a workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A friendly description for the workspace. | 
## Example

```python
from lusid.models.workspace_update_request import WorkspaceUpdateRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

description: StrictStr = "example_description"
workspace_update_request_instance = WorkspaceUpdateRequest(description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

