# PortfolioId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**DataScope**](DataScope.md) |  | [optional] 
**identifier** | **str** |  | [optional] 
## Example

```python
from lusid.models.portfolio_id import PortfolioId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[DataScope] = None
identifier: Optional[StrictStr] = "example_identifier"
portfolio_id_instance = PortfolioId(scope=scope, identifier=identifier)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

