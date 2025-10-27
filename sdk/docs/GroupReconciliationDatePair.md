# GroupReconciliationDatePair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective at date for the reconciliation | [optional] 
**as_at** | **datetime** | The as at date for the reconciliation | [optional] 
## Example

```python
from lusid.models.group_reconciliation_date_pair import GroupReconciliationDatePair
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
group_reconciliation_date_pair_instance = GroupReconciliationDatePair(effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

