# BookTransactionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_ids** | [**List[ResourceId]**](ResourceId.md) | A collection of Allocation IDs | 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A collection of properties | [optional] 
## Example

```python
from lusid.models.book_transactions_request import BookTransactionsRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

allocation_ids: conlist(ResourceId, max_items=5000, min_items=1) = Field(..., alias="allocationIds", description="A collection of Allocation IDs")
transaction_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
book_transactions_request_instance = BookTransactionsRequest(allocation_ids=allocation_ids, transaction_properties=transaction_properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

