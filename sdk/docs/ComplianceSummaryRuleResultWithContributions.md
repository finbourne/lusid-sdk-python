# ComplianceSummaryRuleResultWithContributions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | 
**status** | **str** |  | 
**check_type** | **str** | The kind of check the rule applied across its groups: \&quot;PercentCheck\&quot; or \&quot;Check\&quot;. Static per rule. Absent for a  rule no check reached. | [optional] 
**affected_portfolios** | [**List[ResourceId]**](ResourceId.md) |  | 
**affected_orders** | [**List[ResourceId]**](ResourceId.md) | The orders the rule affected. Omitted for a holdings-based run. | [optional] 
**groups** | [**List[ComplianceRuleBreakdownWithContributions]**](ComplianceRuleBreakdownWithContributions.md) |  | 
**other_positions_considered** | [**List[ComplianceRuleContribution]**](ComplianceRuleContribution.md) | The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in a group&#39;s contributions. Together with those  contributions this forms the whole basis, with no overlap, so a breach can be explained against the full picture  (e.g. the non-equity remainder behind an equity limit). Omitted when the rule evaluated everything it considered. | [optional] 
## Example

```python
from lusid.models.compliance_summary_rule_result_with_contributions import ComplianceSummaryRuleResultWithContributions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: ResourceId = # Replace with your value
status: StrictStr = "example_status"
check_type: Optional[StrictStr] = "example_check_type"
affected_portfolios: List[ResourceId] = # Replace with your value
affected_orders: Optional[List[ResourceId]] = # Replace with your value
groups: List[ComplianceRuleBreakdownWithContributions]
other_positions_considered: Optional[List[ComplianceRuleContribution]] = # Replace with your value
compliance_summary_rule_result_with_contributions_instance = ComplianceSummaryRuleResultWithContributions(rule_id=rule_id, status=status, check_type=check_type, affected_portfolios=affected_portfolios, affected_orders=affected_orders, groups=groups, other_positions_considered=other_positions_considered)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

