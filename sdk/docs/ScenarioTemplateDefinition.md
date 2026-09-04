# ScenarioTemplateDefinition

One pre-built scenario template: the name to pass to CreateScenarioFromTemplate, what the  template does, and the parameters it accepts. A parameter not listed here is rejected by  the create call, not ignored.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The template name, as accepted by CreateScenarioFromTemplate. | [optional] 
**description** | **str** | What the template&#39;s scenario does. | [optional] 
**parameters** | [**List[ScenarioTemplateParameter]**](ScenarioTemplateParameter.md) | The parameters the template accepts, in the order they are documented. Parameter names are  case-sensitive; supplying one not in this list fails the create call. | [optional] 
## Example

```python
from lusid.models.scenario_template_definition import ScenarioTemplateDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
parameters: Optional[List[ScenarioTemplateParameter]] = # Replace with your value
scenario_template_definition_instance = ScenarioTemplateDefinition(name=name, description=description, parameters=parameters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

