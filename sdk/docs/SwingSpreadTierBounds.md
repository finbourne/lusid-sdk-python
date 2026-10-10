# SwingSpreadTierBounds

The bounds of the spread tier a net cashflow fell in.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_bound_exclusive** | **float** | The tier&#39;s lower bound, which the net cashflow was above. | 
**upper_bound_inclusive** | **float** | The tier&#39;s upper bound, which the net cashflow was at or below. Absent for the unbounded last tier. | [optional] 
## Example

```python
from lusid.models.swing_spread_tier_bounds import SwingSpreadTierBounds
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lower_bound_exclusive: Union[StrictFloat, StrictInt] = # Replace with your value
upper_bound_inclusive: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
swing_spread_tier_bounds_instance = SwingSpreadTierBounds(lower_bound_exclusive=lower_bound_exclusive, upper_bound_inclusive=upper_bound_inclusive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

