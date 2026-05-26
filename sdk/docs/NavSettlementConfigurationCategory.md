# NavSettlementConfigurationCategory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculate_instruction_to_portfolio_rate** | **bool** | An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. | [optional] 
**calculate_trade_date_to_settlement_fx_pn_l** | **bool** | An optional flag that allows for the calculation of FxPnL between Trade and Settlement Date. | [optional] 
## Example

```python
from lusid.models.nav_settlement_configuration_category import NavSettlementConfigurationCategory
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calculate_instruction_to_portfolio_rate: Optional[StrictBool] = # Replace with your value
calculate_instruction_to_portfolio_rate:Optional[StrictBool] = None
calculate_trade_date_to_settlement_fx_pn_l: Optional[StrictBool] = # Replace with your value
calculate_trade_date_to_settlement_fx_pn_l:Optional[StrictBool] = None
nav_settlement_configuration_category_instance = NavSettlementConfigurationCategory(calculate_instruction_to_portfolio_rate=calculate_instruction_to_portfolio_rate, calculate_trade_date_to_settlement_fx_pn_l=calculate_trade_date_to_settlement_fx_pn_l)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

