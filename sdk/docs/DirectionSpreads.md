# DirectionSpreads

The tiers of spread for one direction of net cashflow and what their bounds measure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basis** | **str** | What the tier bounds measure: Amount, the size of the net cashflow in the fund currency, or PctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. Available values: Amount, PctOfNav. | 
**tiers** | [**List[SwingSpreadTier]**](SwingSpreadTier.md) | The tiers, in ascending order. Each starts where the previous one ends, and only the last is unbounded above. The first tier&#39;s lower bound is the threshold: a flow at or below it does not swing. | 
## Example

```python
from lusid.models.direction_spreads import DirectionSpreads
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

basis: StrictStr = "example_basis"
tiers: List[SwingSpreadTier] = # Replace with your value
direction_spreads_instance = DirectionSpreads(basis=basis, tiers=tiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

