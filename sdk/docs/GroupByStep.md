# GroupByStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 
## Example

```python
from lusid.models.group_by_step import GroupByStep
from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, constr, validator

label: StrictStr = "example_label"
parameters: conlist(ComplianceTemplateParameter) = # Replace with your value
compliance_step_type: StrictStr = "example_compliance_step_type"
group_by_step_instance = GroupByStep(label=label, parameters=parameters, compliance_step_type=compliance_step_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

