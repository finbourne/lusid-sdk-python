# QuantityInstructed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **float** |  | 
## Example

```python
from lusid.models.quantity_instructed import QuantityInstructed
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, constr

type: StrictStr = "example_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
quantity_instructed_instance = QuantityInstructed(type=type, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

