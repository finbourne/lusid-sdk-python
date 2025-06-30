# GroupReconciliationRunDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_status** | **str** | Provides the reconciliation completion status \&quot;Completed\&quot; | \&quot;FailedToComplete\&quot; | 
**error_detail** | **str** | Error information if the reconciliation failed to complete | [optional] 
## Example

```python
from lusid.models.group_reconciliation_run_details import GroupReconciliationRunDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

completion_status: StrictStr = "example_completion_status"
error_detail: Optional[StrictStr] = "example_error_detail"
group_reconciliation_run_details_instance = GroupReconciliationRunDetails(completion_status=completion_status, error_detail=error_detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

