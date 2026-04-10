# PortfolioWeight

Represents a portfolio and its target allocation weight.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**weight** | **float** | The relative weight of the Portfolio compared to the other Portfolios specified, used to determine the allocation split between Portfolios when there are no Orders within the Block to allocate to. | 
## Example

```python
from lusid.models.portfolio_weight import PortfolioWeight
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
weight: Union[StrictFloat, StrictInt] = # Replace with your value
portfolio_weight_instance = PortfolioWeight(portfolio_id=portfolio_id, weight=weight)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

