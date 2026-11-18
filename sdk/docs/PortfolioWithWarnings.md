# PortfolioWithWarnings

A portfolio together with warnings about its configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio** | [**Portfolio**](Portfolio.md) |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_with_warnings import PortfolioWithWarnings
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio: Optional[Portfolio] = None
warnings: Optional[List[Warning]] = None
links: Optional[List[Link]] = None
portfolio_with_warnings_instance = PortfolioWithWarnings(portfolio=portfolio, warnings=warnings, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

