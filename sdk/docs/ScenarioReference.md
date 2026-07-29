# ScenarioReference

A reference to a stored Scenario, identified by scope and code, optionally pinned to an AsAt version.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the scenario to apply. | 
**code** | **str** | The code of the scenario to apply. | 
**as_at** | **datetime** | The AsAt of the scenario version to apply. If not supplied, the latest version is used. | [optional] 
## Example

```python
from lusid.models.scenario_reference import ScenarioReference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
as_at: Optional[datetime] = # Replace with your value
scenario_reference_instance = ScenarioReference(scope=scope, code=code, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

