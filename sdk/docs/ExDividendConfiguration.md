# ExDividendConfiguration

Configure the ex-dividend periods for the instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_business_days** | **bool** | Is the ex-dividend period counted in business days or calendar days. Defaults to false if not set. | [optional] 
**ex_dividend_days** | **int** | Number of days in the ex-dividend period. If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative. If set, this must be a non-negative number. If not set, or set to 0, than there is no ex-dividend period. | 
**return_negative_accrued** | **bool** | Does the accrued interest go negative in the ex-dividend period, or does it go to zero. | [optional] 
**apply_thirty360_pay_delay** | **bool** | Set this flag to true if the ex-dividend days represent a pay delay from the accrual end date in calendar days under the 30/360 day count convention. The typical use case for this flag are Mortgage Backed Securities with pay delay between 1 and 60 days, such as FreddieMac and FannieMae. If this flag is set, the useBusinessDays setting will be ignored. Defaults to false if not provided. | [optional] 
## Example

```python
from lusid.models.ex_dividend_configuration import ExDividendConfiguration
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt

use_business_days: Optional[StrictBool] = # Replace with your value
use_business_days:Optional[StrictBool] = None
ex_dividend_days: StrictInt = # Replace with your value
ex_dividend_days: StrictInt = 42
return_negative_accrued: Optional[StrictBool] = # Replace with your value
return_negative_accrued:Optional[StrictBool] = None
apply_thirty360_pay_delay: Optional[StrictBool] = # Replace with your value
apply_thirty360_pay_delay:Optional[StrictBool] = None
ex_dividend_configuration_instance = ExDividendConfiguration(use_business_days=use_business_days, ex_dividend_days=ex_dividend_days, return_negative_accrued=return_negative_accrued, apply_thirty360_pay_delay=apply_thirty360_pay_delay)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

