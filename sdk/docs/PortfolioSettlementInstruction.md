# PortfolioSettlementInstruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**portfolio_scope** | **str** | The portfolio scope of the given entity | 
**portfolio_code** | **str** | The portfolio code of the given entity | 
**settlement_instruction_id** | **str** | The settlement instruction Id of the SettlementInstruction being adjusted | 
**nav_activity_adjustment_type** | **str** | . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity | 
## Example

```python
from lusid.models.portfolio_settlement_instruction import PortfolioSettlementInstruction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: datetime = # Replace with your value
portfolio_scope: StrictStr = "example_portfolio_scope"
portfolio_code: StrictStr = "example_portfolio_code"
settlement_instruction_id: StrictStr = "example_settlement_instruction_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
portfolio_settlement_instruction_instance = PortfolioSettlementInstruction(as_at=as_at, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, settlement_instruction_id=settlement_instruction_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

