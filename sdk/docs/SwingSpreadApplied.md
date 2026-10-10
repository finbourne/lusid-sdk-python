# SwingSpreadApplied

The stored spread applied to a share class's baseline price and the tier it came from.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bps** | **float** | The spread applied, in basis points. | 
**tier_matched** | [**SwingSpreadTierBounds**](SwingSpreadTierBounds.md) |  | 
## Example

```python
from lusid.models.swing_spread_applied import SwingSpreadApplied
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bps: Union[StrictFloat, StrictInt] = # Replace with your value
tier_matched: SwingSpreadTierBounds = # Replace with your value
swing_spread_applied_instance = SwingSpreadApplied(bps=bps, tier_matched=tier_matched)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

