# BucketCashFlowDrillDownResponse

The cash flows inside one bucket, with the bucket's balances as the ladder of QueryBucketedCashFlows has them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[CashFlowDetail]**](CashFlowDetail.md) |  | 
**href** | **str** |  | [optional] 
**report_currency** | **str** | The report currency the converted fields are in; absent when none was requested. | [optional] 
**balances** | [**List[BucketCashFlowBalance]**](BucketCashFlowBalance.md) | The bucket&#39;s opening balance, activity and closing balance per payment currency, in the payment currency, in the report  currency when one was requested, and net of haircut when haircut rules were supplied. Absent when no WindowStart was supplied, and when a BucketingSchedule was  supplied: the Buckets and CurrencySubtotals carry the balances then. | [optional] 
**next_page** | **str** | The next page of results: never present, as the cash flows of a bucket are not paged; kept so this response is a superset of the list it replaces. | [optional] 
**previous_page** | **str** | The previous page of results: never present; see NextPage. | [optional] 
**issues** | **List[str]** | Why balances, or report currency figures, are absent when they were asked for; absent when there is nothing to report. | [optional] 
**window_start** | **datetime** | The window start the buckets&#39; balances run from. Present with BucketingSchedule. | [optional] 
**effective_at** | **datetime** | The valuation date the cash flows were evaluated at. Present with BucketingSchedule. | [optional] 
**start_inclusive** | **bool** | Whether a cash flow paid exactly on a bucket&#39;s start is in it. Present with BucketingSchedule. | [optional] 
**end_inclusive** | **bool** | Whether a cash flow paid exactly on a bucket&#39;s end is in it. Present with BucketingSchedule. | [optional] 
**buckets** | [**List[BucketCashFlowBucket]**](BucketCashFlowBucket.md) | One bucket per period of the schedule, per member portfolio, payment currency and sub-holding key combination, each with its  opening balance, closing balance and activity. Present only when a BucketingSchedule was supplied. | [optional] 
**currency_subtotals** | [**List[BucketCurrencySubtotal]**](BucketCurrencySubtotal.md) | The buckets summed across portfolios and sub-holding keys, one per period and payment currency. Present only with Buckets. | [optional] 
**subtotal** | [**BucketCashFlowSubtotal**](BucketCashFlowSubtotal.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_cash_flow_drill_down_response import BucketCashFlowDrillDownResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[CashFlowDetail]
href: Optional[StrictStr] = "example_href"
report_currency: Optional[StrictStr] = "example_report_currency"
balances: Optional[List[BucketCashFlowBalance]] = # Replace with your value
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
issues: Optional[List[StrictStr]] = # Replace with your value
window_start: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
start_inclusive: Optional[StrictBool] = # Replace with your value
start_inclusive:Optional[StrictBool] = None
end_inclusive: Optional[StrictBool] = # Replace with your value
end_inclusive:Optional[StrictBool] = None
buckets: Optional[List[BucketCashFlowBucket]] = # Replace with your value
currency_subtotals: Optional[List[BucketCurrencySubtotal]] = # Replace with your value
subtotal: Optional[BucketCashFlowSubtotal] = None
links: Optional[List[Link]] = None
bucket_cash_flow_drill_down_response_instance = BucketCashFlowDrillDownResponse(values=values, href=href, report_currency=report_currency, balances=balances, next_page=next_page, previous_page=previous_page, issues=issues, window_start=window_start, effective_at=effective_at, start_inclusive=start_inclusive, end_inclusive=end_inclusive, buckets=buckets, currency_subtotals=currency_subtotals, subtotal=subtotal, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

