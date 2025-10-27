# UpsertComplianceRunSummaryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**results** | [**List[ComplianceSummaryRuleResult]**](ComplianceSummaryRuleResult.md) |  | 
## Example

```python
from lusid.models.upsert_compliance_run_summary_result import UpsertComplianceRunSummaryResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: ResourceId = # Replace with your value
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
results: List[ComplianceSummaryRuleResult]
upsert_compliance_run_summary_result_instance = UpsertComplianceRunSummaryResult(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, results=results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

