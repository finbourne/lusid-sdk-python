# ComplianceTemplateParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the required Compliance Template Parameter | 
**description** | **str** | The description for the required Compliance Template Parameter | 
**type** | **str** | The type for the required Compliance Template Parameter | 
## Example

```python
from lusid.models.compliance_template_parameter import ComplianceTemplateParameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
description: StrictStr = "example_description"
type: StrictStr = "example_type"
compliance_template_parameter_instance = ComplianceTemplateParameter(name=name, description=description, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

