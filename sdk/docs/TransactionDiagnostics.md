# TransactionDiagnostics

Represents a set of diagnostics per transaction, where applicable.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_display_name** | **str** |  | 
**error_details** | **List[str]** |  | 
## Example

```python
from lusid.models.transaction_diagnostics import TransactionDiagnostics
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

transaction_display_name: StrictStr = "example_transaction_display_name"
error_details: conlist(StrictStr) = # Replace with your value
transaction_diagnostics_instance = TransactionDiagnostics(transaction_display_name=transaction_display_name, error_details=error_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

