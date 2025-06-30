# AccessControlledAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**action** | [**ActionId**](ActionId.md) |  | 
**limited_set** | [**List[IdSelectorDefinition]**](IdSelectorDefinition.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.access_controlled_action import AccessControlledAction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

description: StrictStr = "example_description"
action: ActionId = # Replace with your value
limited_set: Optional[conlist(IdSelectorDefinition)] = # Replace with your value
links: Optional[conlist(Link)] = None
access_controlled_action_instance = AccessControlledAction(description=description, action=action, limited_set=limited_set, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

