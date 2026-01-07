# QuantityInstructed

The quantity of the event that was instructed, represented either as a percentage of the overall holdings or the number of units instructed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of quantity instructed, either Percentage or Units. | 
**amount** | **float** | The actual amount instructed. For Type Percentage, this is between 0 and 100. | 
## Example

```python
from lusid.models.quantity_instructed import QuantityInstructed
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
quantity_instructed_instance = QuantityInstructed(type=type, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

