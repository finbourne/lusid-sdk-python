# ComplianceRuleBreakdownRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** |  | 
**results_used** | **Dict[str, float]** |  | 
**properties_used** | **Dict[str, List[ModelProperty]]** |  | 
**missing_data_information** | **List[str]** |  | 
**lineage** | [**List[LineageMember]**](LineageMember.md) |  | 
## Example

```python
from lusid.models.compliance_rule_breakdown_request import ComplianceRuleBreakdownRequest
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr

group_status: StrictStr = "example_group_status"
results_used: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
properties_used: Dict[str, conlist(ModelProperty)] = # Replace with your value
missing_data_information: conlist(StrictStr) = # Replace with your value
lineage: conlist(LineageMember) = # Replace with your value
compliance_rule_breakdown_request_instance = ComplianceRuleBreakdownRequest(group_status=group_status, results_used=results_used, properties_used=properties_used, missing_data_information=missing_data_information, lineage=lineage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

