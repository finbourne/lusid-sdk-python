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
**cash_flow_calculation_version** | **str** | The version of the cash flow calculation logic to use. Defaults to &#39;1&#39; if not specified. Valid values are &#39;1&#39; and &#39;2&#39;.  &#39;1&#39; is the current production behaviour: cash flows booked as transactions are de-duplicated against the  instrument cash flows by identifier, and movements are treated as factual when they settle on or before the effective date.  &#39;2&#39; resolves cash flows via a deterministic source waterfall (structured result store &gt; transaction &gt; instrument),  classifies cash flows as factual by the transaction trade date (so trades dealt on or before the effective date  that settle afterwards are factual), and applies corporate action date filtering.  Bucketed responses calculated under version &#39;2&#39; always include the bucket interval metadata columns  (&#39;Valuation/Bucket/Start&#39;, &#39;Valuation/Bucket/End&#39;, &#39;Valuation/Bucket/StartInclusive&#39;, &#39;Valuation/Bucket/EndInclusive&#39;),  which are the required input of the bucket cash flow drill-down endpoint. Without a border configuration the  metadata describes the window-clamped interval of cash flow dates that the rounding method allocates to each bucket point. | [optional] 
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
cash_flow_calculation_version: Optional[StrictStr] = "example_cash_flow_calculation_version"
query_cash_flows_request_instance = QueryCashFlowsRequest(as_at=as_at, window_start=window_start, window_end=window_end, portfolio_entity_ids=portfolio_entity_ids, recipe_id=recipe_id, effective_at=effective_at, cash_flow_calculation_version=cash_flow_calculation_version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

