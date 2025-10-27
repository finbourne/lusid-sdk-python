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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_display_name: StrictStr = "example_transaction_display_name"
error_details: List[StrictStr] = # Replace with your value
transaction_diagnostics_instance = TransactionDiagnostics(transaction_display_name=transaction_display_name, error_details=error_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

