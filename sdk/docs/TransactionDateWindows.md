# TransactionDateWindows

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Transaction Date Window for the left side of a reconciliation | 
**right** | **str** | Transaction Date Window for the right side of a reconciliation | 
## Example

```python
from lusid.models.transaction_date_windows import TransactionDateWindows
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: StrictStr = "example_left"
right: StrictStr = "example_right"
transaction_date_windows_instance = TransactionDateWindows(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

