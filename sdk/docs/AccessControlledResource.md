# AccessControlledResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | 
**actions** | [**List[AccessControlledAction]**](AccessControlledAction.md) |  | 
**identifier_parts** | [**List[IdentifierPartSchema]**](IdentifierPartSchema.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.access_controlled_resource import AccessControlledResource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

application: Optional[StrictStr] = "example_application"
name: Optional[StrictStr] = "example_name"
description: StrictStr = "example_description"
actions: List[AccessControlledAction]
identifier_parts: Optional[List[IdentifierPartSchema]] = # Replace with your value
links: Optional[List[Link]] = None
access_controlled_resource_instance = AccessControlledResource(application=application, name=name, description=description, actions=actions, identifier_parts=identifier_parts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

