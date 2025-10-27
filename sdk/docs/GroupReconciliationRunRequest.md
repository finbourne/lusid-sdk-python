# GroupReconciliationRunRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Reconciliation run Id. Consists of run type (manual or workflow) and identifier. | 
**dates_to_reconcile** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_run_request import GroupReconciliationRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_id: StrictStr = "example_instance_id"
dates_to_reconcile: Optional[GroupReconciliationDates] = # Replace with your value
group_reconciliation_run_request_instance = GroupReconciliationRunRequest(instance_id=instance_id, dates_to_reconcile=dates_to_reconcile)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

