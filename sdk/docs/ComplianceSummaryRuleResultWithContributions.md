# ComplianceSummaryRuleResultWithContributions

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
**rule_breakdown** | [**List[ComplianceRuleBreakdownWithContributions]**](ComplianceRuleBreakdownWithContributions.md) |  | 
**other_positions_considered** | [**List[ComplianceRuleContribution]**](ComplianceRuleContribution.md) | The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in the RuleBreakdown&#39;s  contributions. Together with those contributions this forms the whole basis, with no overlap, so a  breach can be explained against the full picture (e.g. the non-equity remainder behind an equity limit).  Empty when the rule evaluated everything it considered. | 
## Example

```python
from lusid.models.compliance_summary_rule_result_with_contributions import ComplianceSummaryRuleResultWithContributions
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
rule_breakdown: List[ComplianceRuleBreakdownWithContributions] = # Replace with your value
other_positions_considered: List[ComplianceRuleContribution] = # Replace with your value
compliance_summary_rule_result_with_contributions_instance = ComplianceSummaryRuleResultWithContributions(rule_id=rule_id, template_id=template_id, variation=variation, rule_status=rule_status, affected_portfolios=affected_portfolios, affected_orders=affected_orders, parameters_used=parameters_used, rule_breakdown=rule_breakdown, other_positions_considered=other_positions_considered)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

