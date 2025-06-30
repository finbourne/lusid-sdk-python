# TransactionPrice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**type** | **str** | The available values are: Price, Yield, Spread, CashFlowPerUnit, CleanPrice, DirtyPrice | [optional] 
## Example

```python
from lusid.models.transaction_price import TransactionPrice
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

price: Optional[Union[StrictFloat, StrictInt]] = None
type: Optional[StrictStr] = "example_type"
transaction_price_instance = TransactionPrice(price=price, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

