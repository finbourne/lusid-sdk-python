# BatchUpsertPortfolioTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Transaction]**](Transaction.md) | The transactions which have been successfully upserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The transactions that could not be upserted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_portfolio_transactions_response import BatchUpsertPortfolioTransactionsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

values: Optional[Dict[str, Transaction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
batch_upsert_portfolio_transactions_response_instance = BatchUpsertPortfolioTransactionsResponse(values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

