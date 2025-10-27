# QueryInstrumentEventsRequest

Instrument event query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**effective_at** | **datetime** | The Effective date used in the valuation of the cashflows. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**filter_instrument_events** | **str** | Expression to filter the result set. | [optional] 
## Example

```python
from lusid.models.query_instrument_events_request import QueryInstrumentEventsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
effective_at: datetime = # Replace with your value
recipe_id: ResourceId = # Replace with your value
filter_instrument_events: Optional[StrictStr] = "example_filter_instrument_events"
query_instrument_events_request_instance = QueryInstrumentEventsRequest(as_at=as_at, window_start=window_start, window_end=window_end, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, recipe_id=recipe_id, filter_instrument_events=filter_instrument_events)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

