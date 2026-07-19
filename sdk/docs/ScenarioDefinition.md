# ScenarioDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**shifts** | [**List[ScenarioShiftDefinition]**](ScenarioShiftDefinition.md) |  | [optional] 
## Example

```python
from lusid.models.scenario_definition import ScenarioDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
shifts: Optional[List[ScenarioShiftDefinition]] = None
scenario_definition_instance = ScenarioDefinition(scope=scope, code=code, display_name=display_name, description=description, shifts=shifts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

