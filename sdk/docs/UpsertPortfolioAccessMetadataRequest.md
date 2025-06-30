# UpsertPortfolioAccessMetadataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to portfolios that match the identifier | 
## Example

```python
from lusid.models.upsert_portfolio_access_metadata_request import UpsertPortfolioAccessMetadataRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

metadata: conlist(AccessMetadataValue) = # Replace with your value
upsert_portfolio_access_metadata_request_instance = UpsertPortfolioAccessMetadataRequest(metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

