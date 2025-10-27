# PortfolioEntityId

Specification of a portfolio or portfolio group id, its scope and which it is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope within which the portfolio or portfolio group lives. | 
**code** | **str** | Portfolio name or code. | 
**portfolio_entity_type** | **str** | String identifier for portfolio e.g. \&quot;SinglePortfolio\&quot; and \&quot;GroupPortfolio\&quot;. If not specified, it is assumed to be a single portfolio. | [optional] 
## Example

```python
from lusid.models.portfolio_entity_id import PortfolioEntityId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
portfolio_entity_type: Optional[StrictStr] = "example_portfolio_entity_type"
portfolio_entity_id_instance = PortfolioEntityId(scope=scope, code=code, portfolio_entity_type=portfolio_entity_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

