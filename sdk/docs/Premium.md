# Premium

A class containing information for a given premium payment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Premium amount. | 
**currency** | **str** | Premium currency. | 
**var_date** | **datetime** | Date when premium paid. | 
## Example

```python
from lusid.models.premium import Premium
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
var_date: datetime = # Replace with your value
premium_instance = Premium(amount=amount, currency=currency, var_date=var_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

