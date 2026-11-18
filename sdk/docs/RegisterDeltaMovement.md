# RegisterDeltaMovement

A register balance delta one of a transaction type's movements carries, as the engine books it, named by that movement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The holding property key of the register balance, for example PaidInCapital or UncalledCommitment. | 
**direction** | **str** | The direction the balance moves in when the type is booked, the movement&#39;s own direction folded into the delta&#39;s. Available values: Increase, Decrease. | 
**source** | **str** | The movement figure the delta moves the balance by. Available values: Amount, Units, PortfolioAmount, ProportionOfBalance, PortfolioAmountAtAverageRate. | 
**movement_name** | **str** | The name of the movement that carries the delta. | [optional] 
**side** | **str** | The side of the movement that carries the delta. | 
## Example

```python
from lusid.models.register_delta_movement import RegisterDeltaMovement
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
direction: StrictStr = "example_direction"
source: StrictStr = "example_source"
movement_name: Optional[StrictStr] = "example_movement_name"
side: StrictStr = "example_side"
register_delta_movement_instance = RegisterDeltaMovement(key=key, direction=direction, source=source, movement_name=movement_name, side=side)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

