# CreateTradeTicketsResponse

Batch trade ticket creation response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[LusidTradeTicket]**](LusidTradeTicket.md) |  | 
**failures** | [**List[ErrorDetail]**](ErrorDetail.md) |  | 
## Example

```python
from lusid.models.create_trade_tickets_response import CreateTradeTicketsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[LusidTradeTicket]
failures: List[ErrorDetail]
create_trade_tickets_response_instance = CreateTradeTicketsResponse(values=values, failures=failures)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

