# BucketNetOfHaircutBalance

A bucket's balances with the haircut taken. The starting balance is not haircut; each cash flow is net of its haircut, and  so the opening balance is net of the haircuts on the cash flows before the bucket.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**report_currency** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_net_of_haircut_balance import BucketNetOfHaircutBalance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local: Optional[BucketBalanceFigures] = None
report_currency: Optional[BucketBalanceFigures] = # Replace with your value
links: Optional[List[Link]] = None
bucket_net_of_haircut_balance_instance = BucketNetOfHaircutBalance(local=local, report_currency=report_currency, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

