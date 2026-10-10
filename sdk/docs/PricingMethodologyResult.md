# PricingMethodologyResult

What a share class deals at under the fund's pricing methodology at a valuation point, the working behind it, and  the reporting prices the fund publishes for it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dealing** | [**SinglePriceDealing**](SinglePriceDealing.md) |  | [optional] 
**audit** | [**PricingMethodologyAudit**](PricingMethodologyAudit.md) |  | [optional] 
**dual_dealing** | [**DualPriceDealing**](DualPriceDealing.md) |  | [optional] 
**reporting** | **Dict[str, Optional[float]]** | The Fund&#39;s reporting prices for the share class, keyed by label and rounded as the unit price is. A price is absent when the class has no units in issue or the valuation recipe does not publish it. Absent when the Fund has no reporting prices. | [optional] 
## Example

```python
from lusid.models.pricing_methodology_result import PricingMethodologyResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dealing: Optional[SinglePriceDealing] = None
audit: Optional[PricingMethodologyAudit] = None
dual_dealing: Optional[DualPriceDealing] = # Replace with your value
reporting: Optional[Dict[str, Optional[Union[StrictFloat, StrictInt]]]] = # Replace with your value
pricing_methodology_result_instance = PricingMethodologyResult(dealing=dealing, audit=audit, dual_dealing=dual_dealing, reporting=reporting)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

