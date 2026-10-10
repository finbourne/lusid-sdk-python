# SwingSpreadTier

One tier of spread: the band of net cashflow it covers and the spread applied when the flow falls in it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_bound_exclusive** | **float** | The size of net cashflow, as a magnitude, above which the tier applies. Zero or more; zero on the first tier swings on any net flow. | 
**upper_bound_inclusive** | **float** | The size of net cashflow, as a magnitude, up to and including which the tier applies. Omit it on the last tier, which covers every larger flow. | [optional] 
**bps** | **float** | The spread, in basis points of the baseline price, applied when the net cashflow falls in the tier. Zero or more. | 
## Example

```python
from lusid.models.swing_spread_tier import SwingSpreadTier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lower_bound_exclusive: Union[StrictFloat, StrictInt] = # Replace with your value
upper_bound_inclusive: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bps: Union[StrictFloat, StrictInt] = # Replace with your value
swing_spread_tier_instance = SwingSpreadTier(lower_bound_exclusive=lower_bound_exclusive, upper_bound_inclusive=upper_bound_inclusive, bps=bps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

