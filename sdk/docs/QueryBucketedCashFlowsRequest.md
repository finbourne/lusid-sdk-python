# QueryBucketedCashFlowsRequest

Query for bucketed cashflows from one or more portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**window_start** | **datetime** | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified. | 
**window_end** | **datetime** | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to &#39;today&#39; if it is not specified | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**effective_at** | **datetime** | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**rounding_method** | **str** | When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. | 
**bucketing_dates** | **List[datetime]** | A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty. | [optional] 
**bucketing_tenors** | **List[str]** | A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. | 
**group_by** | **List[str]** | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**addresses** | **List[str]** | The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones. | [optional] 
**equip_with_subtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**exclude_unsettled_trades** | **bool** | Flag directing the Valuation call to exclude cashflows from unsettled trades.  If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] 
**cash_flow_type** | **str** | Indicate the requested cash flow representation InstrumentCashFlows or PortfolioCashFlows (GetCashLadder uses this)  Options: [InstrumentCashFlow, PortfolioCashFlow] | [optional] 
**bucketing_schedule** | [**BucketingSchedule**](BucketingSchedule.md) |  | [optional] 
**filter** | **str** |  | [optional] 
## Example

```python
from lusid.models.query_bucketed_cash_flows_request import QueryBucketedCashFlowsRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from datetime import datetime
as_at: Optional[datetime] = # Replace with your value
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
portfolio_entity_ids: conlist(PortfolioEntityId) = # Replace with your value
effective_at: datetime = # Replace with your value
recipe_id: ResourceId = # Replace with your value
rounding_method: StrictStr = "example_rounding_method"
bucketing_dates: Optional[conlist(datetime)] = # Replace with your value
bucketing_tenors: Optional[conlist(StrictStr)] = # Replace with your value
report_currency: StrictStr = "example_report_currency"
group_by: Optional[conlist(StrictStr)] = # Replace with your value
addresses: Optional[conlist(StrictStr)] = # Replace with your value
equip_with_subtotals: Optional[StrictBool] = # Replace with your value
equip_with_subtotals:Optional[StrictBool] = None
exclude_unsettled_trades: Optional[StrictBool] = # Replace with your value
exclude_unsettled_trades:Optional[StrictBool] = None
cash_flow_type: Optional[StrictStr] = "example_cash_flow_type"
bucketing_schedule: Optional[BucketingSchedule] = # Replace with your value
filter: Optional[StrictStr] = "example_filter"
query_bucketed_cash_flows_request_instance = QueryBucketedCashFlowsRequest(as_at=as_at, window_start=window_start, window_end=window_end, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, recipe_id=recipe_id, rounding_method=rounding_method, bucketing_dates=bucketing_dates, bucketing_tenors=bucketing_tenors, report_currency=report_currency, group_by=group_by, addresses=addresses, equip_with_subtotals=equip_with_subtotals, exclude_unsettled_trades=exclude_unsettled_trades, cash_flow_type=cash_flow_type, bucketing_schedule=bucketing_schedule, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

