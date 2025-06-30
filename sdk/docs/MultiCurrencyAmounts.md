# MultiCurrencyAmounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_amount** | **float** |  | 
**base_amount** | **float** |  | 
## Example

```python
from lusid.models.multi_currency_amounts import MultiCurrencyAmounts
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

local_amount: Union[StrictFloat, StrictInt] = # Replace with your value
base_amount: Union[StrictFloat, StrictInt] = # Replace with your value
multi_currency_amounts_instance = MultiCurrencyAmounts(local_amount=local_amount, base_amount=base_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

