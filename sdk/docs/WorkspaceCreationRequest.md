# WorkspaceCreationRequest

A request to create an empty workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A workspace&#39;s name. | 
**description** | **str** | A friendly description for the workspace. | 
## Example

```python
from lusid.models.workspace_creation_request import WorkspaceCreationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
description: StrictStr = "example_description"
workspace_creation_request_instance = WorkspaceCreationRequest(name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

