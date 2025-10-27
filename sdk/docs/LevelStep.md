# LevelStep

Item which is stepped in level/quantity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date from which the level should apply. | 
**quantity** | **float** | The quantity which is applied. This might be an absolute, percentage, fractional or other value. | 
## Example

```python
from lusid.models.level_step import LevelStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
level_step_instance = LevelStep(var_date=var_date, quantity=quantity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

