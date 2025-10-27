# ComplianceSummaryRuleResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**variation** | **str** |  | 
**rule_status** | **str** |  | 
**affected_portfolios** | [**List[ResourceId]**](ResourceId.md) |  | 
**affected_orders** | [**List[ResourceId]**](ResourceId.md) |  | 
**parameters_used** | **Dict[str, Optional[str]]** |  | 
**rule_breakdown** | [**List[ComplianceRuleBreakdown]**](ComplianceRuleBreakdown.md) |  | 
## Example

```python
from lusid.models.compliance_summary_rule_result import ComplianceSummaryRuleResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: ResourceId = # Replace with your value
template_id: ResourceId = # Replace with your value
variation: StrictStr = "example_variation"
rule_status: StrictStr = "example_rule_status"
affected_portfolios: List[ResourceId] = # Replace with your value
affected_orders: List[ResourceId] = # Replace with your value
parameters_used: Dict[str, Optional[StrictStr]] = # Replace with your value
rule_breakdown: List[ComplianceRuleBreakdown] = # Replace with your value
compliance_summary_rule_result_instance = ComplianceSummaryRuleResult(rule_id=rule_id, template_id=template_id, variation=variation, rule_status=rule_status, affected_portfolios=affected_portfolios, affected_orders=affected_orders, parameters_used=parameters_used, rule_breakdown=rule_breakdown)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

