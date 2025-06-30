# ComplianceRuleBreakdown

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** | The status of this subset of results. | 
**results_used** | **Dict[str, float]** | Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule. | 
**properties_used** | **Dict[str, List[ModelProperty]]** | Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule | 
**missing_data_information** | **List[str]** | List of string information detailing data that was missing from contributions processed in this rule | 
**lineage** | [**List[LineageMember]**](LineageMember.md) |  | 
## Example

```python
from lusid.models.compliance_rule_breakdown import ComplianceRuleBreakdown
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr

group_status: StrictStr = "example_group_status"
results_used: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
properties_used: Dict[str, conlist(ModelProperty)] = # Replace with your value
missing_data_information: conlist(StrictStr) = # Replace with your value
lineage: conlist(LineageMember) = # Replace with your value
compliance_rule_breakdown_instance = ComplianceRuleBreakdown(group_status=group_status, results_used=results_used, properties_used=properties_used, missing_data_information=missing_data_information, lineage=lineage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

