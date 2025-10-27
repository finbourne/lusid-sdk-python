# BatchUpsertPortfolioAccessMetadataResponseItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**metadata** | **Dict[str, Optional[List[AccessMetadataValue]]]** |  | 
## Example

```python
from lusid.models.batch_upsert_portfolio_access_metadata_response_item import BatchUpsertPortfolioAccessMetadataResponseItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
metadata: Dict[str, Optional[List[AccessMetadataValue]]]
batch_upsert_portfolio_access_metadata_response_item_instance = BatchUpsertPortfolioAccessMetadataResponseItem(portfolio_id=portfolio_id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

