# BucketCashFlowBalance

The balances of a bucket in one payment currency and, when a report currency was requested, in the report currency, and,  when haircut rules were supplied, net of the haircuts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The payment currency of the cash flows. Balances of different currencies are never added together. | [optional] 
**local** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**report_currency** | [**BucketBalanceFigures**](BucketBalanceFigures.md) |  | [optional] 
**starting_balance_rate** | **float** | With an FxRateType other than FxSpot, the spot rate that converts the ladder&#39;s starting balance in this currency into the report currency, when that balance is not zero: the spot as at the window start for FxSpotAtCashFlowDate (or as at the valuation date when the window starts after it, as nothing is known of a later spot rate), and as at the valuation date for FxForward and ForwardThenSpot. | [optional] 
**net_of_haircut** | [**BucketNetOfHaircutBalance**](BucketNetOfHaircutBalance.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_cash_flow_balance import BucketCashFlowBalance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency: Optional[StrictStr] = "example_currency"
local: Optional[BucketBalanceFigures] = None
report_currency: Optional[BucketBalanceFigures] = # Replace with your value
starting_balance_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_of_haircut: Optional[BucketNetOfHaircutBalance] = # Replace with your value
links: Optional[List[Link]] = None
bucket_cash_flow_balance_instance = BucketCashFlowBalance(currency=currency, local=local, report_currency=report_currency, starting_balance_rate=starting_balance_rate, net_of_haircut=net_of_haircut, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

