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
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist, constr

keys: conlist(PerpetualProperty, min_items=1) = Field(...)
value_type: StrictStr = "example_value_type"
value: Union[StrictFloat, StrictInt] = # Replace with your value
strategy_instance = Strategy(keys=keys, value_type=value_type, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

