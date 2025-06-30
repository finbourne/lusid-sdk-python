# IUnitDefinitionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**code** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
## Example

```python
from lusid.models.i_unit_definition_dto import IUnitDefinitionDto
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

var_schema: Optional[StrictStr] = "example_var_schema"
code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
i_unit_definition_dto_instance = IUnitDefinitionDto(var_schema=var_schema, code=code, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

