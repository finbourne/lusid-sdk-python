# PortfolioReconciliationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **str** | The effective date of the portfolio | 
**as_at** | **datetime** | Optional. The AsAt date of the portfolio | [optional] 
## Example

```python
from lusid.models.portfolio_reconciliation_request import PortfolioReconciliationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
effective_at: StrictStr = "example_effective_at"
as_at: Optional[datetime] = # Replace with your value
portfolio_reconciliation_request_instance = PortfolioReconciliationRequest(portfolio_id=portfolio_id, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

