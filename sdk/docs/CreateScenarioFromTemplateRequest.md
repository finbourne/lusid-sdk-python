# CreateScenarioFromTemplateRequest

Request to create a scenario from a pre-built parameterised template. The template determines the  shape of the scenario's shifts; the parameters supply the targets (e.g. currency, instrument) and  optionally override the template's default shift size.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | The template to build the scenario from. Available templates: RatesUp, RatesDown, CurveSteepener,  CurveFlattener, VolSpike, EquityCrash, FxShock, RiskOff. | 
**code** | **str** | The code of the scenario to create. | 
**display_name** | **str** | The display name of the created scenario. Defaults to a name derived from the template. | [optional] 
**description** | **str** | The description of the created scenario. Defaults to a description derived from the template. | [optional] 
**parameters** | **Dict[str, Optional[str]]** | Template parameters. Which parameters are required depends on the template: &#39;ccy&#39; for rate curve  templates, &#39;instrument&#39; for equity and vol templates, &#39;currencyPair&#39; for FX templates; RiskOff  requires &#39;ccy&#39; and &#39;instrument&#39;. All templates accept an optional &#39;amount&#39; override of the  template&#39;s default shift size. | [optional] 
## Example

```python
from lusid.models.create_scenario_from_template_request import CreateScenarioFromTemplateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

template: StrictStr = "example_template"
code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
parameters: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
create_scenario_from_template_request_instance = CreateScenarioFromTemplateRequest(template=template, code=code, display_name=display_name, description=description, parameters=parameters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

