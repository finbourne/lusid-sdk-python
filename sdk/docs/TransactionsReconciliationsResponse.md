# TransactionsReconciliationsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**Mapping**](Mapping.md) |  | [optional] 
**data** | [**List[ReconciledTransaction]**](ReconciledTransaction.md) | The result of this reconciliation | [optional] 
## Example

```python
from lusid.models.transactions_reconciliations_response import TransactionsReconciliationsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

mapping: Optional[Mapping] = None
data: Optional[conlist(ReconciledTransaction)] = # Replace with your value
transactions_reconciliations_response_instance = TransactionsReconciliationsResponse(mapping=mapping, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

