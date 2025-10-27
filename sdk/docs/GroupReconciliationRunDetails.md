# GroupReconciliationRunDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_status** | **str** | Provides the reconciliation completion status \&quot;Completed\&quot; | \&quot;FailedToComplete\&quot; | 
**error_detail** | **str** | Error information if the reconciliation failed to complete | [optional] 
## Example

```python
from lusid.models.group_reconciliation_run_details import GroupReconciliationRunDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

completion_status: StrictStr = "example_completion_status"
error_detail: Optional[StrictStr] = "example_error_detail"
group_reconciliation_run_details_instance = GroupReconciliationRunDetails(completion_status=completion_status, error_detail=error_detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

