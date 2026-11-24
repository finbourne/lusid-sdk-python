# MissingMovementOption

A movement option one of a transaction type's line legs must carry for the register to see what it books, and does not, named by that movement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_name** | **str** | The name of the movement that carries the delta. | [optional] 
**side** | **str** | The side of the movement that carries the delta. | 
**option** | **str** | The movement option the leg lacks. Currently always &#39;Registry&#39;. | 
## Example

```python
from lusid.models.missing_movement_option import MissingMovementOption
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

movement_name: Optional[StrictStr] = "example_movement_name"
side: StrictStr = "example_side"
option: StrictStr = "example_option"
missing_movement_option_instance = MissingMovementOption(movement_name=movement_name, side=side, option=option)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

