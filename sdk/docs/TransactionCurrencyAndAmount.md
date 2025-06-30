# TransactionCurrencyAndAmount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
## Example

```python
from lusid.models.transaction_currency_and_amount import TransactionCurrencyAndAmount
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, constr

currency: Optional[StrictStr] = "example_currency"
amount: Optional[StrictStr] = "example_amount"
transaction_currency_and_amount_instance = TransactionCurrencyAndAmount(currency=currency, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

