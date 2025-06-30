# CreateUnitDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**details** | **Dict[str, str]** |  | [optional] 
## Example

```python
from lusid.models.create_unit_definition import CreateUnitDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
details: Optional[Dict[str, StrictStr]] = None
create_unit_definition_instance = CreateUnitDefinition(code=code, display_name=display_name, description=description, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

