# PercentCheckStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**limit_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for an absolute limit check | 
**warning_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for a warning limit check | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 
## Example

```python
from lusid.models.percent_check_step import PercentCheckStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: StrictStr = "example_label"
limit_check_parameters: List[ComplianceTemplateParameter] = # Replace with your value
warning_check_parameters: List[ComplianceTemplateParameter] = # Replace with your value
compliance_step_type: StrictStr = "example_compliance_step_type"
percent_check_step_instance = PercentCheckStep(label=label, limit_check_parameters=limit_check_parameters, warning_check_parameters=warning_check_parameters, compliance_step_type=compliance_step_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

