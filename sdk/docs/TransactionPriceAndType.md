# TransactionPriceAndType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
## Example

```python
from lusid.models.transaction_price_and_type import TransactionPriceAndType
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, constr

price: Optional[StrictStr] = "example_price"
type: Optional[StrictStr] = "example_type"
transaction_price_and_type_instance = TransactionPriceAndType(price=price, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

