# BucketCashFlowDrillDownResponse

The cash flows of a range of effective dates, split into periods by a BucketingSchedule: for each period, member portfolio,  payment currency and sub-holding key combination, its opening balance, the cash flows that make up its activity, and its  closing balance. Each balance and each cash flow appears once, in its bucket.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_currency** | **str** | The report currency the cash flows&#39; converted fields are in; absent when none was requested. | [optional] 
**window_start** | **datetime** | The window start the buckets&#39; balances run from: where the first bucket&#39;s opening balance is taken. | 
**buckets** | [**List[BucketCashFlowBucket]**](BucketCashFlowBucket.md) | One bucket per period of the schedule, per member portfolio, payment currency and sub-holding key combination, each with its  opening balance, activity and closing balance. | 
**currency_subtotals** | [**List[BucketCurrencySubtotal]**](BucketCurrencySubtotal.md) | The buckets summed across portfolios and sub-holding keys, one per period and payment currency. | 
**issues** | **List[str]** | What the balances do not cover, for example that they are in the payment currency only and gross of haircut; absent when there is nothing to report. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_cash_flow_drill_down_response import BucketCashFlowDrillDownResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

report_currency: Optional[StrictStr] = "example_report_currency"
window_start: datetime = # Replace with your value
buckets: List[BucketCashFlowBucket] = # Replace with your value
currency_subtotals: List[BucketCurrencySubtotal] = # Replace with your value
issues: Optional[List[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
bucket_cash_flow_drill_down_response_instance = BucketCashFlowDrillDownResponse(report_currency=report_currency, window_start=window_start, buckets=buckets, currency_subtotals=currency_subtotals, issues=issues, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

