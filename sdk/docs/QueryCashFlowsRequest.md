# QueryCashFlowsRequest

Query for cashflows from one or more portfolios
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **datetime** | The Effective date used in the valuation of the cashflows. | 
## Example

```python
from lusid.models.query_cash_flows_request import QueryCashFlowsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
recipe_id: ResourceId = # Replace with your value
effective_at: datetime = # Replace with your value
query_cash_flows_request_instance = QueryCashFlowsRequest(as_at=as_at, window_start=window_start, window_end=window_end, portfolio_entity_ids=portfolio_entity_ids, recipe_id=recipe_id, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

