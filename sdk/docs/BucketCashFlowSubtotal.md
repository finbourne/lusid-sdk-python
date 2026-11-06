# BucketCashFlowSubtotal

The balances of a bucket summed across all payment currencies, in the report currency. It carries only report currency  figures, as a total across currencies has no meaning in any single payment currency, and no rate, as there is no single rate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_currency** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**net_of_haircut** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_cash_flow_subtotal import BucketCashFlowSubtotal
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

report_currency: Optional[BucketBalanceFigures] = # Replace with your value
net_of_haircut: Optional[BucketBalanceFigures] = # Replace with your value
links: Optional[List[Link]] = None
bucket_cash_flow_subtotal_instance = BucketCashFlowSubtotal(report_currency=report_currency, net_of_haircut=net_of_haircut, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

