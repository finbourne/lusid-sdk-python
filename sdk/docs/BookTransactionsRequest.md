# BookTransactionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_ids** | [**List[ResourceId]**](ResourceId.md) | A collection of Allocation IDs | 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A collection of properties | [optional] 
## Example

```python
from lusid.models.book_transactions_request import BookTransactionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allocation_ids: List[ResourceId] = # Replace with your value
transaction_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
book_transactions_request_instance = BookTransactionsRequest(allocation_ids=allocation_ids, transaction_properties=transaction_properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

