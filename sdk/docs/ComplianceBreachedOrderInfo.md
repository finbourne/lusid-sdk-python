# ComplianceBreachedOrderInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**list_rule_result** | [**List[ComplianceRuleResult]**](ComplianceRuleResult.md) | The Rule Results for a particular compliance run | 
## Example

```python
from lusid.models.compliance_breached_order_info import ComplianceBreachedOrderInfo
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

order_id: ResourceId = # Replace with your value
list_rule_result: conlist(ComplianceRuleResult) = # Replace with your value
compliance_breached_order_info_instance = ComplianceBreachedOrderInfo(order_id=order_id, list_rule_result=list_rule_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

