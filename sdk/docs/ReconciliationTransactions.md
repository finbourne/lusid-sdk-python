# ReconciliationTransactions

Specification for the transactions of a scheduled reconciliation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_window** | [**DateRange**](DateRange.md) |  | [optional] 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.reconciliation_transactions import ReconciliationTransactions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_window: Optional[DateRange] = # Replace with your value
mapping_id: Optional[ResourceId] = # Replace with your value
reconciliation_transactions_instance = ReconciliationTransactions(transaction_window=transaction_window, mapping_id=mapping_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

