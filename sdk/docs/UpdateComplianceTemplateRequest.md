# UpdateComplianceTemplateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Compliance Template | 
**description** | **str** | The description of the Compliance Template | 
**variations** | [**List[ComplianceTemplateVariationRequest]**](ComplianceTemplateVariationRequest.md) | Variation details of a Compliance Template | 
## Example

```python
from lusid.models.update_compliance_template_request import UpdateComplianceTemplateRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

code: StrictStr = "example_code"
description: StrictStr = "example_description"
variations: conlist(ComplianceTemplateVariationRequest) = # Replace with your value
update_compliance_template_request_instance = UpdateComplianceTemplateRequest(code=code, description=description, variations=variations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

