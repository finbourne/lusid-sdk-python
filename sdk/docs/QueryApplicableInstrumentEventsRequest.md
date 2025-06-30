# QueryApplicableInstrumentEventsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**effective_at** | **datetime** | The Effective date that splits query window into two parts: factual period and forecast period | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**forecasting_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.query_applicable_instrument_events_request import QueryApplicableInstrumentEventsRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
effective_at: datetime = # Replace with your value
portfolio_entity_ids: conlist(PortfolioEntityId) = # Replace with your value
forecasting_recipe_id: ResourceId = # Replace with your value
query_applicable_instrument_events_request_instance = QueryApplicableInstrumentEventsRequest(window_start=window_start, window_end=window_end, effective_at=effective_at, portfolio_entity_ids=portfolio_entity_ids, forecasting_recipe_id=forecasting_recipe_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

