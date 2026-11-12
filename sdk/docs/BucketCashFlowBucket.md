# BucketCashFlowBucket

One tenor bucket for one portfolio, payment currency and set of sub-holding keys: its opening balance, closing balance and the  cash flows that make up its activity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Identifies the bucket: a 32 character lowercase hexadecimal hash of its period (start and end), payment currency, portfolio and sub-holding keys. It is stable, the same bucket has the same id in every response, and it is opaque: compare it, do not take it apart. | [optional] 
**bucket_start** | **datetime** | The start of the period the bucket covers. | [optional] 
**bucket_end** | **datetime** | The end of the period the bucket covers. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**currency** | **str** | The payment currency of the bucket. | [optional] 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding keys the bucket is for, limited to those the caller may read. | [optional] 
**open** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**activity_total** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**activity** | [**List[CashFlowDetail]**](CashFlowDetail.md) | The cash flows in the bucket, with the attributes a cash flow has in Values. | [optional] 
**close** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_cash_flow_bucket import BucketCashFlowBucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: Optional[StrictStr] = "example_bucket_id"
bucket_start: Optional[datetime] = # Replace with your value
bucket_end: Optional[datetime] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
open: Optional[BucketAmounts] = None
activity_total: Optional[BucketAmounts] = # Replace with your value
activity: Optional[List[CashFlowDetail]] = # Replace with your value
close: Optional[BucketAmounts] = None
links: Optional[List[Link]] = None
bucket_cash_flow_bucket_instance = BucketCashFlowBucket(bucket_id=bucket_id, bucket_start=bucket_start, bucket_end=bucket_end, portfolio_id=portfolio_id, currency=currency, sub_holding_keys=sub_holding_keys, open=open, activity_total=activity_total, activity=activity, close=close, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

