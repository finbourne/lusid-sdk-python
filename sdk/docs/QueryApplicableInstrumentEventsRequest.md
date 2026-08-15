# QueryApplicableInstrumentEventsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**effective_at** | **datetime** | The Effective date that splits query window into two parts: factual period and forecast period. Optional - a timeline (with an optional closed period) may be supplied instead to derive the effective date. | [optional] 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**forecasting_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**timeline_scope** | **str** | The scope of the timeline to be used when building the instrument events. | [optional] 
**timeline_code** | **str** | The code of the timeline to be used when building the instrument events. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. | [optional] 
**closed_period_id** | **str** | The id of the closed period, on the given timeline, to be used when building the instrument events. | [optional] 
## Example

```python
from lusid.models.query_applicable_instrument_events_request import QueryApplicableInstrumentEventsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
forecasting_recipe_id: ResourceId = # Replace with your value
timeline_scope: Optional[StrictStr] = "example_timeline_scope"
timeline_code: Optional[StrictStr] = "example_timeline_code"
closed_period_id: Optional[StrictStr] = "example_closed_period_id"
query_applicable_instrument_events_request_instance = QueryApplicableInstrumentEventsRequest(window_start=window_start, window_end=window_end, effective_at=effective_at, portfolio_entity_ids=portfolio_entity_ids, forecasting_recipe_id=forecasting_recipe_id, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

