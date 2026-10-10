# SwingPolicy

The baseline a Single fund's dealing price starts from, the spreads it swings by and, for a Market swing, the  triggers that say when it swings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**SwingBaseline**](SwingBaseline.md) |  | 
**default_spread_source** | **str** | Where the swing comes from. Stored swings by the tiers in spreads. Market swings to the bid or offer, including notional dealing costs, that the valuation recipe of each active NAV type publishes, when the net cashflow passes inflowTrigger or outflowTrigger. Omit it for a fund that never swings and always deals at its baseline. Available values: Stored, Market. | [optional] 
**spreads** | [**SwingSpreads**](SwingSpreads.md) |  | [optional] 
**inflow_trigger** | [**SwingTrigger**](SwingTrigger.md) |  | [optional] 
**outflow_trigger** | [**SwingTrigger**](SwingTrigger.md) |  | [optional] 
## Example

```python
from lusid.models.swing_policy import SwingPolicy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

baseline: SwingBaseline
default_spread_source: Optional[StrictStr] = "example_default_spread_source"
spreads: Optional[SwingSpreads] = None
inflow_trigger: Optional[SwingTrigger] = # Replace with your value
outflow_trigger: Optional[SwingTrigger] = # Replace with your value
swing_policy_instance = SwingPolicy(baseline=baseline, default_spread_source=default_spread_source, spreads=spreads, inflow_trigger=inflow_trigger, outflow_trigger=outflow_trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

