# ComplianceTemplateVariationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**description** | **str** |  | 
**outcome_description** | **str** |  | [optional] 
**referenced_group_label** | **str** |  | [optional] 
**steps** | [**List[ComplianceStepRequest]**](ComplianceStepRequest.md) |  | 
## Example

```python
from lusid.models.compliance_template_variation_request import ComplianceTemplateVariationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

label: StrictStr = "example_label"
description: StrictStr = "example_description"
outcome_description: Optional[StrictStr] = "example_outcome_description"
referenced_group_label: Optional[StrictStr] = "example_referenced_group_label"
steps: conlist(ComplianceStepRequest) = # Replace with your value
compliance_template_variation_request_instance = ComplianceTemplateVariationRequest(label=label, description=description, outcome_description=outcome_description, referenced_group_label=referenced_group_label, steps=steps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

