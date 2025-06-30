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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

application: Optional[StrictStr] = "example_application"
name: Optional[StrictStr] = "example_name"
description: StrictStr = "example_description"
actions: conlist(AccessControlledAction) = # Replace with your value
identifier_parts: Optional[conlist(IdentifierPartSchema)] = # Replace with your value
links: Optional[conlist(Link)] = None
access_controlled_resource_instance = AccessControlledResource(application=application, name=name, description=description, actions=actions, identifier_parts=identifier_parts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

