# BookTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Transaction]**](Transaction.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 
**fx_orders** | [**List[BlockAndOrders]**](BlockAndOrders.md) |  | [optional] 
## Example

```python
from lusid.models.book_transactions_response import BookTransactionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, Transaction]] = None
failed: Optional[Dict[str, ErrorDetail]] = None
fx_orders: Optional[List[BlockAndOrders]] = # Replace with your value
book_transactions_response_instance = BookTransactionsResponse(values=values, failed=failed, fx_orders=fx_orders)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

