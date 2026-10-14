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
**report_currency** | **str** | Optional three letter ISO currency string to convert cashflow amounts into. When supplied, each returned cashflow additionally carries ReportCurrencyAmount and TradeToReportCurrencyRate, converted from its own payment (instrument) currency. When omitted, those two fields are not present on any cashflow: Amount (always in the cashflow&#39;s own payment currency) are unaffected either way. | [optional] 
**exclude_unsettled_trades** | **bool** | If set to true, unsettled trades are excluded from the result set. Set this to match the value used on the bucketed cash flow query being drilled into, so the individual cash flows reconcile with the bucket. Note that the drill-down returns the complete resolved stream including transaction-sourced cashflows; if the bucketed query used the (default) InstrumentCashFlow representation, also exclude rows with a sourceType of &#39;Transaction&#39; when reconciling. | [optional] 
**haircut_rules** | [**List[CashFlowHaircutRule]**](CashFlowHaircutRule.md) | Optional ordered haircut rules applied to cashflow inflows; the first matching rule wins and a rule with no criteria acts as a catch-all. When supplied, each returned cashflow carries its gross amount, haircut fraction, net amount and the rule that was applied; with no rules those fields are omitted and the results are unchanged. | [optional] 
**cash_type** | **str** | Which date basis buckets cash flows: TradeDate uses each cash flow&#39;s transaction date, SettleDate (default) uses its payment date. The response&#39;s CashFlowDetail.PaymentDate reflects whichever basis was used. Available values: TradeDate, SettleDate. | [optional] 
**fx_rate_type** | **str** | Which FX rate converts each cashflow into the ReportCurrency. FxSpot (default) uses the spot rate. FxForward uses the forward rate for the cashflow&#39;s payment date, read from the FX forward curve the recipe resolves for the currency pair as at the valuation (EffectiveAt) date; a cashflow with no such forward rate reports an Error and has no converted amount. ForwardThenSpot uses the forward rate where the recipe resolves one and the spot rate where it does not. FxForward and ForwardThenSpot require a ReportCurrency. A cashflow paid after the last point of the recipe&#39;s forward curve takes the last point&#39;s forward rate when the curve&#39;s back extrapolation is Flat (the default), and reports an Error when it is None. Where ForwardThenSpot falls back, the spot rate is the one FxSpot uses: read on the cashflow&#39;s own transaction date, not the valuation date. The response&#39;s CashFlowDetail.FxRateTypeApplied says which rate each cashflow received. Available values: FxSpot, FxForward, ForwardThenSpot. | [optional] 
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
report_currency: Optional[StrictStr] = "example_report_currency"
exclude_unsettled_trades: Optional[StrictBool] = # Replace with your value
exclude_unsettled_trades:Optional[StrictBool] = None
haircut_rules: Optional[List[CashFlowHaircutRule]] = # Replace with your value
cash_type: Optional[StrictStr] = "example_cash_type"
fx_rate_type: Optional[StrictStr] = "example_fx_rate_type"
query_bucket_cash_flow_drill_down_request_instance = QueryBucketCashFlowDrillDownRequest(as_at=as_at, bucket_start=bucket_start, bucket_end=bucket_end, start_inclusive=start_inclusive, end_inclusive=end_inclusive, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, recipe_id=recipe_id, report_currency=report_currency, exclude_unsettled_trades=exclude_unsettled_trades, haircut_rules=haircut_rules, cash_type=cash_type, fx_rate_type=fx_rate_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

