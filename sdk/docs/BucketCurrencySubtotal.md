# BucketCurrencySubtotal

A bucket's balances for one payment currency, summed across portfolios and sub-holding keys.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_start** | **datetime** | The start of the period the subtotal covers. | [optional] 
**bucket_end** | **datetime** | The end of the period the subtotal covers. | [optional] 
**currency** | **str** | The payment currency. | [optional] 
**open** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**activity_total** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**close** | [**BucketAmounts**](BucketAmounts.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_currency_subtotal import BucketCurrencySubtotal
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_start: Optional[datetime] = # Replace with your value
bucket_end: Optional[datetime] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
open: Optional[BucketAmounts] = None
activity_total: Optional[BucketAmounts] = # Replace with your value
close: Optional[BucketAmounts] = None
links: Optional[List[Link]] = None
bucket_currency_subtotal_instance = BucketCurrencySubtotal(bucket_start=bucket_start, bucket_end=bucket_end, currency=currency, open=open, activity_total=activity_total, close=close, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

