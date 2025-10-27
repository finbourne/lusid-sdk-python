# Strategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[PerpetualProperty]**](PerpetualProperty.md) |  | 
**value_type** | **str** |  | 
**value** | **float** |  | 
## Example

```python
from lusid.models.strategy import Strategy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

keys: List[PerpetualProperty]
value_type: StrictStr = "example_value_type"
value: Union[StrictFloat, StrictInt]
strategy_instance = Strategy(keys=keys, value_type=value_type, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

