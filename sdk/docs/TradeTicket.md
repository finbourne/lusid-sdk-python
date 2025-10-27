# TradeTicket

The base class for representing a Trade Ticket in LUSID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_ticket_type** | **str** | The available values are: LusidTradeTicket, ExternalTradeTicket | 
## Example

```python
from lusid.models.trade_ticket import TradeTicket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trade_ticket_type: StrictStr = "example_trade_ticket_type"
trade_ticket_instance = TradeTicket(trade_ticket_type=trade_ticket_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

