# BookTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Transaction]**](Transaction.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 
## Example

```python
from lusid.models.book_transactions_response import BookTransactionsResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel

values: Optional[Dict[str, Transaction]] = None
failed: Optional[Dict[str, ErrorDetail]] = None
book_transactions_response_instance = BookTransactionsResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

