# WorkspaceItem

An item stored in a workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the workspace item. | 
**format** | **int** | A simple integer format identifier. | 
**name** | **str** | A workspace item&#39;s name. | 
**group** | **str** | The group containing a workspace item. | 
**description** | **str** | The description of a workspace item. | 
**content** | **object** | The content associated with a workspace item. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.workspace_item import WorkspaceItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
format: StrictInt = # Replace with your value
format: StrictInt = 42
name: StrictStr = "example_name"
group: StrictStr = "example_group"
description: StrictStr = "example_description"
content: Optional[Any] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
workspace_item_instance = WorkspaceItem(type=type, format=format, name=name, group=group, description=description, content=content, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

