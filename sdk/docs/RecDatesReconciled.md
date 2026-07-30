# RecDatesReconciled

The left and right effective and asAt dates of the data reconciled in a run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_effective_at** | **datetime** | The effective datetime of the data reconciled on the left side. | 
**left_as_at** | **datetime** | The asAt datetime of the data reconciled on the left side. | 
**right_effective_at** | **datetime** | The effective datetime of the data reconciled on the right side. | 
**right_as_at** | **datetime** | The asAt datetime of the data reconciled on the right side. | 
## Example

```python
from lusid.models.rec_dates_reconciled import RecDatesReconciled
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left_effective_at: datetime = # Replace with your value
left_as_at: datetime = # Replace with your value
right_effective_at: datetime = # Replace with your value
right_as_at: datetime = # Replace with your value
rec_dates_reconciled_instance = RecDatesReconciled(left_effective_at=left_effective_at, left_as_at=left_as_at, right_effective_at=right_effective_at, right_as_at=right_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

