# ComplianceRuleUpsertResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ComplianceRule]**](ComplianceRule.md) |  | 
## Example

```python
from lusid.models.compliance_rule_upsert_response import ComplianceRuleUpsertResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Dict[str, ComplianceRule]
compliance_rule_upsert_response_instance = ComplianceRuleUpsertResponse(values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

