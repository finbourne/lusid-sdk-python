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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: StrictStr = "example_label"
description: StrictStr = "example_description"
outcome_description: Optional[StrictStr] = "example_outcome_description"
referenced_group_label: Optional[StrictStr] = "example_referenced_group_label"
steps: List[ComplianceStepRequest]
compliance_template_variation_request_instance = ComplianceTemplateVariationRequest(label=label, description=description, outcome_description=outcome_description, referenced_group_label=referenced_group_label, steps=steps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

