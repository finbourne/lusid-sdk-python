# ComplianceStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 
## Example

```python
from lusid.models.compliance_step import ComplianceStep
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

compliance_step_type: StrictStr = "example_compliance_step_type"
compliance_step_instance = ComplianceStep(compliance_step_type=compliance_step_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

