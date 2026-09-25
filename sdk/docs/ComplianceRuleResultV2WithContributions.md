# ComplianceRuleResultV2WithContributions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** | Available values: PreTrade, PostTrade, PreAndPostTrade. | 
**rule_result** | [**ComplianceSummaryRuleResultWithContributions**](ComplianceSummaryRuleResultWithContributions.md) |  | 
## Example

```python
from lusid.models.compliance_rule_result_v2_with_contributions import ComplianceRuleResultV2WithContributions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: ResourceId = # Replace with your value
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
rule_result: ComplianceSummaryRuleResultWithContributions = # Replace with your value
compliance_rule_result_v2_with_contributions_instance = ComplianceRuleResultV2WithContributions(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, rule_result=rule_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

