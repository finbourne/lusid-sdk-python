# BondDefaultSuppressionDetails

Which parts of the instrument the default suspends, and by what fraction: 0.0 is fully suppressed and 1.0  unaffected, applying from the default's effective date onwards. An empty block suppresses nothing - every  unset field means 1.0. Omitting the block entirely is different: that cancels coupons and principal  outright from the default onwards, while interest keeps accruing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual_percentage** | **float** | Fraction of interest accruing from the default&#39;s effective date onwards, between 0.0 and 1.0. Interest  accrued before that date is unaffected, and a later default restates the fraction from its own date.  Accrued interest supplied through a results store is returned unchanged. Optional, defaulting to 1.0. | [optional] 
**coupon_percentage** | **float** | Fraction of each coupon from the default onwards that is still paid, between 0.0 and 1.0. Optional,  defaulting to 1.0. | [optional] 
**principal_percentage** | **float** | Fraction of each principal repayment from the default onwards still paid, between 0.0 and 1.0.  Optional, defaulting to 1.0. | [optional] 
## Example

```python
from lusid.models.bond_default_suppression_details import BondDefaultSuppressionDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

accrual_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
coupon_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
principal_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bond_default_suppression_details_instance = BondDefaultSuppressionDetails(accrual_percentage=accrual_percentage, coupon_percentage=coupon_percentage, principal_percentage=principal_percentage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

