# SettlementInLieu

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_settlement_currency** | **str** |  | 
**amount** | **float** |  | [optional] 
## Example

```python
from lusid.models.settlement_in_lieu import SettlementInLieu
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

original_settlement_currency: StrictStr = "example_original_settlement_currency"
amount: Optional[Union[StrictFloat, StrictInt]] = None
settlement_in_lieu_instance = SettlementInLieu(original_settlement_currency=original_settlement_currency, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

