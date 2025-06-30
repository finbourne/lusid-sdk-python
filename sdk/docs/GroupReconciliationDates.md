# GroupReconciliationDates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 
**right** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_dates import GroupReconciliationDates
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel

left: Optional[GroupReconciliationDatePair] = None
right: Optional[GroupReconciliationDatePair] = None
group_reconciliation_dates_instance = GroupReconciliationDates(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

