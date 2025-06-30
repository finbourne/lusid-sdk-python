# UpsertPortfolioTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_portfolio_transactions_response import UpsertPortfolioTransactionsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

version: Version = # Replace with your value
href: Optional[StrictStr] = "example_href"
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_portfolio_transactions_response_instance = UpsertPortfolioTransactionsResponse(version=version, href=href, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

