# IdSelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **Dict[str, str]** |  | 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.id_selector_definition import IdSelectorDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

identifier: Dict[str, StrictStr] = # Replace with your value
actions: conlist(ActionId, min_items=1) = Field(...)
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
id_selector_definition_instance = IdSelectorDefinition(identifier=identifier, actions=actions, name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

