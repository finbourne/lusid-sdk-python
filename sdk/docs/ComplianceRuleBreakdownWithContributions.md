# ComplianceRuleBreakdownWithContributions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** | The status of this subset of results. | 
**results_used** | **Dict[str, float]** | Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule. | 
**properties_used** | **Dict[str, Optional[List[ModelProperty]]]** | Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule | 
**missing_data_information** | **List[str]** | List of string information detailing data that was missing from contributions processed in this rule | 
**lineage** | [**List[LineageMember]**](LineageMember.md) |  | 
**contributions** | [**List[ComplianceRuleContribution]**](ComplianceRuleContribution.md) | The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response. | 
## Example

```python
from lusid.models.compliance_rule_breakdown_with_contributions import ComplianceRuleBreakdownWithContributions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_status: StrictStr = "example_group_status"
results_used: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
properties_used: Dict[str, Optional[List[ModelProperty]]] = # Replace with your value
missing_data_information: List[StrictStr] = # Replace with your value
lineage: List[LineageMember]
contributions: List[ComplianceRuleContribution] = # Replace with your value
compliance_rule_breakdown_with_contributions_instance = ComplianceRuleBreakdownWithContributions(group_status=group_status, results_used=results_used, properties_used=properties_used, missing_data_information=missing_data_information, lineage=lineage, contributions=contributions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

