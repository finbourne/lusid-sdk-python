# BondDefaultSuppressionDetails

How much of each component of a bond keeps paying after a default, as a fraction from 0.0 (fully  suppressed) to 1.0 (unaffected). An unset field means 1.0. Omitting the whole section is different: that  suppresses coupons and principal outright and leaves interest accruing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual_percentage** | **float** | Fraction of the computed accrued interest returned from the default onwards, between 0.0 and 1.0.  Accrued interest supplied through a results store is returned unchanged. Optional, defaulting to 1.0. | [optional] 
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

