# Workspace

A workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A workspace&#39;s name. | 
**description** | **str** | A friendly description for the workspace. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.workspace import Workspace
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

name: StrictStr = "example_name"
description: StrictStr = "example_description"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
workspace_instance = Workspace(name=name, description=description, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

