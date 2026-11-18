# ChangeCompositePortfolioMembershipRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**from_date** | **datetime** | The effective date from which the constituent contributes to the composite portfolio. Defaults to the constituent&#39;s creation date, and must not be later than it, because a constituent contributes its whole history. | [optional] 
## Example

```python
from lusid.models.change_composite_portfolio_membership_request import ChangeCompositePortfolioMembershipRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
from_date: Optional[datetime] = # Replace with your value
change_composite_portfolio_membership_request_instance = ChangeCompositePortfolioMembershipRequest(portfolio_id=portfolio_id, from_date=from_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

