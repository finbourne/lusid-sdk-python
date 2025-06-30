# CheckStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**limit_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for an absolute limit check | 
**warning_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for a warning limit check | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 
## Example

```python
from lusid.models.check_step import CheckStep
from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, constr, validator

label: StrictStr = "example_label"
limit_check_parameters: conlist(ComplianceTemplateParameter) = # Replace with your value
warning_check_parameters: conlist(ComplianceTemplateParameter) = # Replace with your value
compliance_step_type: StrictStr = "example_compliance_step_type"
check_step_instance = CheckStep(label=label, limit_check_parameters=limit_check_parameters, warning_check_parameters=warning_check_parameters, compliance_step_type=compliance_step_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

