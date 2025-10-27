# MultiCurrencyAmounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_amount** | **float** |  | 
**base_amount** | **float** |  | 
## Example

```python
from lusid.models.multi_currency_amounts import MultiCurrencyAmounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local_amount: Union[StrictFloat, StrictInt] = # Replace with your value
base_amount: Union[StrictFloat, StrictInt] = # Replace with your value
multi_currency_amounts_instance = MultiCurrencyAmounts(local_amount=local_amount, base_amount=base_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

