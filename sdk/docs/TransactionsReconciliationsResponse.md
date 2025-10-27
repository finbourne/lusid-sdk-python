# TransactionsReconciliationsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**Mapping**](Mapping.md) |  | [optional] 
**data** | [**List[ReconciledTransaction]**](ReconciledTransaction.md) | The result of this reconciliation | [optional] 
## Example

```python
from lusid.models.transactions_reconciliations_response import TransactionsReconciliationsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mapping: Optional[Mapping] = None
data: Optional[List[ReconciledTransaction]] = # Replace with your value
transactions_reconciliations_response_instance = TransactionsReconciliationsResponse(mapping=mapping, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

