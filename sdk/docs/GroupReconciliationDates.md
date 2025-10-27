# GroupReconciliationDates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 
**right** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_dates import GroupReconciliationDates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[GroupReconciliationDatePair] = None
right: Optional[GroupReconciliationDatePair] = None
group_reconciliation_dates_instance = GroupReconciliationDates(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

