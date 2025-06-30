# GroupByStepRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 
## Example

```python
from lusid.models.group_by_step_request import GroupByStepRequest
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator

label: StrictStr = "example_label"
compliance_step_type_request: StrictStr = "example_compliance_step_type_request"
group_by_step_request_instance = GroupByStepRequest(label=label, compliance_step_type_request=compliance_step_type_request)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

