# ComplianceRuleUpsertResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, ComplianceRule]**](ComplianceRule.md) |  | 
## Example

```python
from lusid.models.compliance_rule_upsert_response import ComplianceRuleUpsertResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

values: Dict[str, ComplianceRule] = # Replace with your value
compliance_rule_upsert_response_instance = ComplianceRuleUpsertResponse(values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

