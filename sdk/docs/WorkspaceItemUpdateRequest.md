# WorkspaceItemUpdateRequest

A request to update a workspace item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **int** | A simple integer format identifier. | 
**description** | **str** | The description of a workspace item. | 
**content** | **object** | The content associated with a workspace item. | 
**type** | **str** | The type of the workspace item. | 
## Example

```python
from lusid.models.workspace_item_update_request import WorkspaceItemUpdateRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, constr, validator

format: StrictInt = # Replace with your value
format: StrictInt = 42
description: StrictStr = "example_description"
content: Optional[Any] = # Replace with your value
type: StrictStr = "example_type"
workspace_item_update_request_instance = WorkspaceItemUpdateRequest(format=format, description=description, content=content, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

