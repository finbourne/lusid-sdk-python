# BatchUpsertPortfolioAccessMetadataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, BatchUpsertPortfolioAccessMetadataResponseItem]**](BatchUpsertPortfolioAccessMetadataResponseItem.md) | The items have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The items that could not be updated or created along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_portfolio_access_metadata_response import BatchUpsertPortfolioAccessMetadataResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, BatchUpsertPortfolioAccessMetadataResponseItem]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
batch_upsert_portfolio_access_metadata_response_instance = BatchUpsertPortfolioAccessMetadataResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

