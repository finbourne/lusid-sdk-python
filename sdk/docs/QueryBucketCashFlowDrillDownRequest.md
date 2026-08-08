# QueryBucketCashFlowDrillDownRequest

Query for the individual cashflows inside a single cashflow bucket, with their source lineage.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for cashflows. | [optional] 
**bucket_start** | **datetime** | The lower bound effective datetime of the bucket from which to retrieve the cashflows. | 
**bucket_end** | **datetime** | The upper bound effective datetime of the bucket from which to retrieve the cashflows. | 
**start_inclusive** | **bool** | Whether a cashflow paid exactly on the bucket start is included in the bucket. Defaults to true. | [optional] 
**end_inclusive** | **bool** | Whether a cashflow paid exactly on the bucket end is included in the bucket. Defaults to true. | [optional] 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the cashflows must belong. | 
**effective_at** | **datetime** | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. | 
**exclude_unsettled_trades** | **bool** | If set to true, unsettled trades are excluded from the result set. Set this to match the value used on the bucketed cash flow query being drilled into, so the individual cash flows reconcile with the bucket. | [optional] 
**haircut_rules** | [**List[CashFlowHaircutRule]**](CashFlowHaircutRule.md) | Optional ordered haircut rules applied to cashflow inflows; the first matching rule wins and a rule with no criteria acts as a catch-all. When supplied, each returned cashflow carries its gross amount, haircut fraction, net amount and the rule that was applied; with no rules those fields are omitted and the results are unchanged. | [optional] 
## Example

```python
from lusid.models.query_bucket_cash_flow_drill_down_request import QueryBucketCashFlowDrillDownRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
bucket_start: datetime = # Replace with your value
bucket_end: datetime = # Replace with your value
start_inclusive: Optional[StrictBool] = # Replace with your value
start_inclusive:Optional[StrictBool] = None
end_inclusive: Optional[StrictBool] = # Replace with your value
end_inclusive:Optional[StrictBool] = None
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
effective_at: datetime = # Replace with your value
recipe_id: ResourceId = # Replace with your value
report_currency: StrictStr = "example_report_currency"
exclude_unsettled_trades: Optional[StrictBool] = # Replace with your value
exclude_unsettled_trades:Optional[StrictBool] = None
haircut_rules: Optional[List[CashFlowHaircutRule]] = # Replace with your value
query_bucket_cash_flow_drill_down_request_instance = QueryBucketCashFlowDrillDownRequest(as_at=as_at, bucket_start=bucket_start, bucket_end=bucket_end, start_inclusive=start_inclusive, end_inclusive=end_inclusive, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, recipe_id=recipe_id, report_currency=report_currency, exclude_unsettled_trades=exclude_unsettled_trades, haircut_rules=haircut_rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

