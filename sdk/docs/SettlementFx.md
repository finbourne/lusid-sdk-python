# SettlementFx

The FX gain or loss on a settlement instruction, with its transaction's realised gain or loss.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_currency** | **str** |  | [optional] 
**settlement_amount** | **float** |  | [optional] 
**portfolio_currency_amount** | **float** |  | [optional] 
**trade_date_fx_rate** | **float** |  | [optional] 
**fx_rate_used** | **float** |  | [optional] 
**fx_rate_source** | **str** |  | [optional] 
**fx_gain_loss_on_settlement** | **float** |  | [optional] 
**total_realised_gain_loss_on_transaction** | **float** |  | [optional] 
## Example

```python
from lusid.models.settlement_fx import SettlementFx
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

settlement_currency: Optional[StrictStr] = "example_settlement_currency"
settlement_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
portfolio_currency_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trade_date_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fx_rate_used: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fx_rate_source: Optional[StrictStr] = "example_fx_rate_source"
fx_gain_loss_on_settlement: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
total_realised_gain_loss_on_transaction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_fx_instance = SettlementFx(settlement_currency=settlement_currency, settlement_amount=settlement_amount, portfolio_currency_amount=portfolio_currency_amount, trade_date_fx_rate=trade_date_fx_rate, fx_rate_used=fx_rate_used, fx_rate_source=fx_rate_source, fx_gain_loss_on_settlement=fx_gain_loss_on_settlement, total_realised_gain_loss_on_transaction=total_realised_gain_loss_on_transaction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

