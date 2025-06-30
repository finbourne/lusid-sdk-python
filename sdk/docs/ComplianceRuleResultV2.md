# ComplianceRuleResultV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**rule_result** | [**ComplianceSummaryRuleResult**](ComplianceSummaryRuleResult.md) |  | 
## Example

```python
from lusid.models.compliance_rule_result_v2 import ComplianceRuleResultV2
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
run_id: ResourceId = # Replace with your value
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
rule_result: ComplianceSummaryRuleResult = # Replace with your value
compliance_rule_result_v2_instance = ComplianceRuleResultV2(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, rule_result=rule_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

