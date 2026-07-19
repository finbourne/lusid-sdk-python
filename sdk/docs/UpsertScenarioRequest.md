# UpsertScenarioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | [**ScenarioDefinition**](ScenarioDefinition.md) |  | 
## Example

```python
from lusid.models.upsert_scenario_request import UpsertScenarioRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scenario: ScenarioDefinition
upsert_scenario_request_instance = UpsertScenarioRequest(scenario=scenario)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

