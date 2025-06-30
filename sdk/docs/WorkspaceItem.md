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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, conlist, constr, validator

type: StrictStr = "example_type"
format: StrictInt = # Replace with your value
format: StrictInt = 42
name: StrictStr = "example_name"
group: StrictStr = "example_group"
description: StrictStr = "example_description"
content: Optional[Any] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
workspace_item_instance = WorkspaceItem(type=type, format=format, name=name, group=group, description=description, content=content, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

