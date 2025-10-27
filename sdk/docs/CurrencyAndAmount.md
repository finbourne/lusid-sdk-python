# CurrencyAndAmount

An amount of a specific currency, specifying a value and an associated unit
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | 
## Example

```python
from lusid.models.currency_and_amount import CurrencyAndAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Optional[Union[StrictFloat, StrictInt]] = None
currency: StrictStr = "example_currency"
currency_and_amount_instance = CurrencyAndAmount(amount=amount, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

