# IntermediateComplianceStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**grouped_parameters** | **Dict[str, Optional[List[ComplianceTemplateParameter]]]** | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 
## Example

```python
from lusid.models.intermediate_compliance_step import IntermediateComplianceStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: StrictStr = "example_label"
grouped_parameters: Dict[str, Optional[List[ComplianceTemplateParameter]]] = # Replace with your value
compliance_step_type: StrictStr = "example_compliance_step_type"
intermediate_compliance_step_instance = IntermediateComplianceStep(label=label, grouped_parameters=grouped_parameters, compliance_step_type=compliance_step_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

