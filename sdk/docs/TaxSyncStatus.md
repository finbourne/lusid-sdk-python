# TaxSyncStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolios** | [**List[TaxPortfolioSyncStatus]**](TaxPortfolioSyncStatus.md) | The sync position of each portfolio in the Fund. | 
## Example

```python
from lusid.models.tax_sync_status import TaxSyncStatus
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolios: List[TaxPortfolioSyncStatus] = # Replace with your value
tax_sync_status_instance = TaxSyncStatus(portfolios=portfolios)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

