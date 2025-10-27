# TransactionPrice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**type** | **str** | The available values are: Price, Yield, Spread, CashFlowPerUnit, CleanPrice, DirtyPrice | [optional] 
## Example

```python
from lusid.models.transaction_price import TransactionPrice
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

price: Optional[Union[StrictFloat, StrictInt]] = None
type: Optional[StrictStr] = "example_type"
transaction_price_instance = TransactionPrice(price=price, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

