# ScenarioDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**short_code** | **str** | A short, memorable identifier for the scenario, for use in reporting. Optional on upsert:  when omitted, reads return a value inferred from the display name (falling back to the  code) rather than null; the inferred value is computed fresh on every read and is never  persisted. When supplied, the value is stored and returned verbatim. Independent of  scenarioType. | [optional] 
**scenario_type** | **str** | Classifies the scenario. Required on upsert; supported string (enumeration) values are:  [Historical, Regulatory, Hypothetical]. Independent of shortCode. Available values: Historical, Regulatory, Hypothetical. | 
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
short_code: Optional[StrictStr] = "example_short_code"
scenario_type: StrictStr = "example_scenario_type"
shifts: Optional[List[ScenarioShiftDefinition]] = None
scenario_definition_instance = ScenarioDefinition(scope=scope, code=code, display_name=display_name, description=description, short_code=short_code, scenario_type=scenario_type, shifts=shifts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

