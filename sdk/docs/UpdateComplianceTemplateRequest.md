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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
description: StrictStr = "example_description"
variations: List[ComplianceTemplateVariationRequest] = # Replace with your value
update_compliance_template_request_instance = UpdateComplianceTemplateRequest(code=code, description=description, variations=variations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

