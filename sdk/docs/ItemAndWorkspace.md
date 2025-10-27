# ItemAndWorkspace

An item plus its containing workspace name.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_name** | **str** | A workspace&#39;s name. | 
**workspace_item** | [**WorkspaceItem**](WorkspaceItem.md) |  | 
## Example

```python
from lusid.models.item_and_workspace import ItemAndWorkspace
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

workspace_name: StrictStr = "example_workspace_name"
workspace_item: WorkspaceItem = # Replace with your value
item_and_workspace_instance = ItemAndWorkspace(workspace_name=workspace_name, workspace_item=workspace_item)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

