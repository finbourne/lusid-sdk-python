# QueryTradeTicketsRequest

Query for tradetickets resulting from events on instrument that are taken from one or more portfolios
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for tradetickets. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **datetime** | The Effective date used in the valuation of the tradetickets. | 
## Example

```python
from lusid.models.query_trade_tickets_request import QueryTradeTicketsRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
as_at: Optional[datetime] = # Replace with your value
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
portfolio_entity_ids: conlist(PortfolioEntityId) = # Replace with your value
recipe_id: ResourceId = # Replace with your value
effective_at: datetime = # Replace with your value
query_trade_tickets_request_instance = QueryTradeTicketsRequest(as_at=as_at, window_start=window_start, window_end=window_end, portfolio_entity_ids=portfolio_entity_ids, recipe_id=recipe_id, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

