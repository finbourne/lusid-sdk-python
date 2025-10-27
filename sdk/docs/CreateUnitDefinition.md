# CreateUnitDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**details** | **Dict[str, Optional[str]]** |  | [optional] 
## Example

```python
from lusid.models.create_unit_definition import CreateUnitDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
details: Optional[Dict[str, Optional[StrictStr]]] = None
create_unit_definition_instance = CreateUnitDefinition(code=code, display_name=display_name, description=description, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

