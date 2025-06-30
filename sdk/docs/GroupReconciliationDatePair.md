# GroupReconciliationDatePair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective at date for the reconciliation | [optional] 
**as_at** | **datetime** | The as at date for the reconciliation | [optional] 
## Example

```python
from lusid.models.group_reconciliation_date_pair import GroupReconciliationDatePair
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
group_reconciliation_date_pair_instance = GroupReconciliationDatePair(effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

