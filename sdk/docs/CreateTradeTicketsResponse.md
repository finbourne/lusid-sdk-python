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
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

values: conlist(LusidTradeTicket) = # Replace with your value
failures: conlist(ErrorDetail) = # Replace with your value
create_trade_tickets_response_instance = CreateTradeTicketsResponse(values=values, failures=failures)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

