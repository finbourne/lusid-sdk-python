# MarginRounding

The increment margin calls are rounded to, and the direction for deliveries and returns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The increment margin calls are rounded to. Must be greater than zero. | 
**deliveries** | **str** | How amounts we deliver are rounded. One of Up or Nearest. Available values: Up, Down, Nearest. | 
**returns** | **str** | How amounts we receive back are rounded. One of Down or Nearest. Available values: Up, Down, Nearest. | 
## Example

```python
from lusid.models.margin_rounding import MarginRounding
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Union[StrictFloat, StrictInt] = # Replace with your value
deliveries: StrictStr = "example_deliveries"
returns: StrictStr = "example_returns"
margin_rounding_instance = MarginRounding(amount=amount, deliveries=deliveries, returns=returns)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

