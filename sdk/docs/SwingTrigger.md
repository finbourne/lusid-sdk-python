# SwingTrigger

When a Market swing fires in one direction: the net cashflow measure and the size it must exceed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What the threshold measures: NetCashflowAbsolute, the size of the net cashflow in the fund currency, or NetCashflowPctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. A NetCashflowPctOfNav trigger does not fire when there is no previous NAV. Available values: NetCashflowAbsolute, NetCashflowPctOfNav. | 
**threshold** | **float** | The size of net cashflow, as a magnitude, the flow must be above for the trigger to fire. Above zero. | 
## Example

```python
from lusid.models.swing_trigger import SwingTrigger
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
threshold: Union[StrictFloat, StrictInt] = # Replace with your value
swing_trigger_instance = SwingTrigger(type=type, threshold=threshold)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

