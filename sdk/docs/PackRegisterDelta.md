# PackRegisterDelta

A register balance delta: a partners' capital balance, the direction it moves in once booked and the figure it moves by.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The holding property key of the register balance, for example PaidInCapital or UncalledCommitment. | 
**direction** | **str** | The direction the balance moves in when the type is booked, the movement&#39;s own direction folded into the delta&#39;s. Available values: Increase, Decrease. | 
**source** | **str** | The movement figure the delta moves the balance by. Available values: Amount, Units, PortfolioAmount, ProportionOfBalance, PortfolioAmountAtAverageRate. | 
## Example

```python
from lusid.models.pack_register_delta import PackRegisterDelta
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
direction: StrictStr = "example_direction"
source: StrictStr = "example_source"
pack_register_delta_instance = PackRegisterDelta(key=key, direction=direction, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

