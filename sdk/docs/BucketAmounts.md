# BucketAmounts

An amount in the payment currency and, when a report currency was requested, in the report currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | **float** | The amount in the payment currency. | [optional] 
**report** | **float** | The amount in the report currency; absent when no report currency was requested, or when a rate needed to convert it could not be found or a cash flow could not be converted (the response&#39;s Issues says which). Under the default FxSpot rate type an opening or closing balance is the payment currency balance converted at the spot rate as at the effective date, the rate every cash flow is converted at, so it agrees with the report currency balances QueryBucketedCashFlows gives for the same date. Under any other rate type a balance is a running sum, not the value of the payment currency balance: the starting balance converted at the spot rate (see StartingBalanceRate) plus every cash flow up to that date, each at the rate that rate type gave it. It is the cumulative cash flow in the report currency, so it can have the opposite sign to Local when the rate has moved. Under FxForward a cash flow paid on or before the effective date has no forward rate, so a series with one before the bucket has no report currency balances. In both, Open + ActivityTotal &#x3D; Close and each Close equals the next Open. The activity total is the sum of its cash flows&#39; own report currency amounts. | [optional] 
**rate** | **float** | Under FxSpot, on an opening or closing balance, the spot rate it was converted at. On an activity total, the effective rate, Report divided by Local, which is a blended rate when its cash flows were converted at different rates. Absent when Report is, on a balance under any other rate type (a running sum has no single rate), or when the effective rate&#39;s Local is 0. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_amounts import BucketAmounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
report: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
bucket_amounts_instance = BucketAmounts(local=local, report=report, rate=rate, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

