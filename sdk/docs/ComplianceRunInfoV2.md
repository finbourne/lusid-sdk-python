# ComplianceRunInfoV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**instigated_by** | **str** |  | 
## Example

```python
from lusid.models.compliance_run_info_v2 import ComplianceRunInfoV2
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
run_id: ResourceId = # Replace with your value
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
instigated_by: StrictStr = "example_instigated_by"
compliance_run_info_v2_instance = ComplianceRunInfoV2(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, instigated_by=instigated_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

