# BatchUpsertPortfolioAccessMetadataResponseItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** |  | 
## Example

```python
from lusid.models.batch_upsert_portfolio_access_metadata_response_item import BatchUpsertPortfolioAccessMetadataResponseItem
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

portfolio_id: ResourceId = # Replace with your value
metadata: Dict[str, conlist(AccessMetadataValue)] = # Replace with your value
batch_upsert_portfolio_access_metadata_response_item_instance = BatchUpsertPortfolioAccessMetadataResponseItem(portfolio_id=portfolio_id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

