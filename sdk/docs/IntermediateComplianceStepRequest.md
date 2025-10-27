# IntermediateComplianceStepRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 
## Example

```python
from lusid.models.intermediate_compliance_step_request import IntermediateComplianceStepRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: StrictStr = "example_label"
compliance_step_type_request: StrictStr = "example_compliance_step_type_request"
intermediate_compliance_step_request_instance = IntermediateComplianceStepRequest(label=label, compliance_step_type_request=compliance_step_type_request)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

