# ComplianceRuleBreakdownWithContributions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | A stable identifier for this group within the rule, matching the same group in the rule-result endpoint. | 
**status** | **str** | The status of this subset of results. | 
**group_key** | [**ComplianceGroupKey**](ComplianceGroupKey.md) |  | [optional] 
**nav** | **float** | The portfolio net asset value the group sits within. Absent where no contribution carried it. | [optional] 
**results** | **Dict[str, float]** | The valuation result totals the group aggregated. Omitted when empty. | [optional] 
**comparisons** | [**List[ComplianceComparison]**](ComplianceComparison.md) | Every leaf comparison the check criterion made for this group, drawn from both the hard and the soft limit.  Omitted for a group no check reached. | [optional] 
**properties** | **Dict[str, Optional[List[ModelProperty]]]** | The property values the group aggregated. Omitted when empty. | [optional] 
**formula_values** | **Dict[str, float]** | The value each formula within the check criterion evaluated to for this group. Omitted when empty. | [optional] 
**contributions** | [**List[ComplianceRuleContribution]**](ComplianceRuleContribution.md) | The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response. | 
**missing_data_information** | **List[str]** | List of string information detailing data that was missing from contributions processed in this rule. Omitted when empty. | [optional] 
**contribution_count** | **int** | The number of contributions aggregated into this group, before any cap. | 
**contributions_truncated** | **bool** | Whether the reported contributions were capped below ContributionCount. Always false today. | 
## Example

```python
from lusid.models.compliance_rule_breakdown_with_contributions import ComplianceRuleBreakdownWithContributions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_id: StrictInt = # Replace with your value
group_id: StrictInt = 42
status: StrictStr = "example_status"
group_key: Optional[ComplianceGroupKey] = # Replace with your value
nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
results: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
comparisons: Optional[List[ComplianceComparison]] = # Replace with your value
properties: Optional[Dict[str, Optional[List[ModelProperty]]]] = # Replace with your value
formula_values: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
contributions: List[ComplianceRuleContribution] = # Replace with your value
missing_data_information: Optional[List[StrictStr]] = # Replace with your value
contribution_count: StrictInt = # Replace with your value
contribution_count: StrictInt = 42
contributions_truncated: StrictBool = # Replace with your value
contributions_truncated:StrictBool = True
compliance_rule_breakdown_with_contributions_instance = ComplianceRuleBreakdownWithContributions(group_id=group_id, status=status, group_key=group_key, nav=nav, results=results, comparisons=comparisons, properties=properties, formula_values=formula_values, contributions=contributions, missing_data_information=missing_data_information, contribution_count=contribution_count, contributions_truncated=contributions_truncated)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

