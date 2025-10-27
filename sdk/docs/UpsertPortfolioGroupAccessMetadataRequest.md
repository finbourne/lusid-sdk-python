# UpsertPortfolioGroupAccessMetadataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to portfolio groups that match the identifier | 
## Example

```python
from lusid.models.upsert_portfolio_group_access_metadata_request import UpsertPortfolioGroupAccessMetadataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metadata: List[AccessMetadataValue] = # Replace with your value
upsert_portfolio_group_access_metadata_request_instance = UpsertPortfolioGroupAccessMetadataRequest(metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

