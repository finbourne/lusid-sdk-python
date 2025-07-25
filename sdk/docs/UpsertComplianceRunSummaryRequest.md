# UpsertComplianceRunSummaryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**results** | [**List[ComplianceSummaryRuleResultRequest]**](ComplianceSummaryRuleResultRequest.md) |  | 
## Example

```python
from lusid.models.upsert_compliance_run_summary_request import UpsertComplianceRunSummaryRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr
from datetime import datetime
run_id: ResourceId = # Replace with your value
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
results: conlist(ComplianceSummaryRuleResultRequest) = # Replace with your value
upsert_compliance_run_summary_request_instance = UpsertComplianceRunSummaryRequest(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, results=results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

