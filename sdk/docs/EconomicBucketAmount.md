# EconomicBucketAmount

An amount in one economic bucket, in the holding's currency and the portfolio currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | The economic bucket, such as &#39;NA_Cost&#39;, &#39;NA_Accrued&#39;, &#39;PL_Carry&#39; or &#39;PL_RealPriceGL&#39;. | [optional] 
**component** | **str** | The component of the economic bucket, such as &#39;TradedInterest&#39;, &#39;Income&#39;, &#39;Expense&#39; or &#39;CoreMarket&#39;. Null where the bucket has no component. | [optional] 
**variant** | **str** | The variant of the economic bucket, such as &#39;Bought&#39;, &#39;Sold&#39;, &#39;Coupon&#39;, &#39;Dividend&#39;, &#39;Fee&#39;, &#39;Tax&#39;, &#39;ShortTerm&#39; or &#39;LongTerm&#39;. Null where the bucket has no variant. | [optional] 
**local** | **float** | The amount in the holding&#39;s currency. | [optional] 
**portfolio** | **float** | The amount in the portfolio currency. | [optional] 
## Example

```python
from lusid.models.economic_bucket_amount import EconomicBucketAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket: Optional[StrictStr] = "example_bucket"
component: Optional[StrictStr] = "example_component"
variant: Optional[StrictStr] = "example_variant"
local: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
portfolio: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
economic_bucket_amount_instance = EconomicBucketAmount(bucket=bucket, component=component, variant=variant, local=local, portfolio=portfolio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

