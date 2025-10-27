# IdSelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **Dict[str, Optional[str]]** |  | 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.id_selector_definition import IdSelectorDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifier: Dict[str, Optional[StrictStr]]
actions: List[ActionId]
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
id_selector_definition_instance = IdSelectorDefinition(identifier=identifier, actions=actions, name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

