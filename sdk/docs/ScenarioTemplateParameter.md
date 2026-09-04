# ScenarioTemplateParameter

One parameter of a scenario template: its name (case-sensitive), whether it must be supplied,  what it means, and - for optional numeric parameters - the default used when omitted and the  unit the value is read in.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The parameter name, as supplied in the create request&#39;s Parameters dictionary. Case-sensitive. | [optional] 
**required** | **bool** | Whether the parameter must be supplied. | [optional] 
**description** | **str** | What the parameter means to this template. | [optional] 
**default_value** | **str** | The value used when the parameter is omitted. Null for required parameters. | [optional] 
**unit** | **str** | The unit a numeric value is read in: &#39;BasisPoints&#39;, &#39;PercentagePoints&#39; or &#39;Fraction&#39;  (0.20 meaning +20%). The templates do NOT share one unit - read this per template.  Null for non-numeric parameters. | [optional] 
**exclusive_group** | **str** | Parameters of a template sharing an ExclusiveGroup are alternatives: exactly one of them must  be supplied. Group members are not individually Required and carry no default. Null for  parameters that stand alone. | [optional] 
## Example

```python
from lusid.models.scenario_template_parameter import ScenarioTemplateParameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
default_value: Optional[StrictStr] = "example_default_value"
unit: Optional[StrictStr] = "example_unit"
exclusive_group: Optional[StrictStr] = "example_exclusive_group"
scenario_template_parameter_instance = ScenarioTemplateParameter(name=name, required=required, description=description, default_value=default_value, unit=unit, exclusive_group=exclusive_group)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

