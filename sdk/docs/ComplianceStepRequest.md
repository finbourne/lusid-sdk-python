# ComplianceStepRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 
## Example

```python
from lusid.models.compliance_step_request import ComplianceStepRequest
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

compliance_step_type_request: StrictStr = "example_compliance_step_type_request"
compliance_step_request_instance = ComplianceStepRequest(compliance_step_type_request=compliance_step_type_request)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

