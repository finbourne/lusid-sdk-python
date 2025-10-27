# PortfolioTradeTicket

Response for querying trade tickets
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**trade_ticket** | [**LusidTradeTicket**](LusidTradeTicket.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_trade_ticket import PortfolioTradeTicket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_portfolio_id: Optional[ResourceId] = # Replace with your value
trade_ticket: Optional[LusidTradeTicket] = # Replace with your value
portfolio_trade_ticket_instance = PortfolioTradeTicket(source_portfolio_id=source_portfolio_id, trade_ticket=trade_ticket)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

