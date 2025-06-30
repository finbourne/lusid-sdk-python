# TransactionDateWindows

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Transaction Date Window for the left side of a reconciliation | 
**right** | **str** | Transaction Date Window for the right side of a reconciliation | 
## Example

```python
from lusid.models.transaction_date_windows import TransactionDateWindows
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

left: StrictStr = "example_left"
right: StrictStr = "example_right"
transaction_date_windows_instance = TransactionDateWindows(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

