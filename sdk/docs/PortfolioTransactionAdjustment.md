# PortfolioTransactionAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav_activity_adjustment_source** | **str** | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. | 
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**portfolio_scope** | **str** | The portfolio scope of the given entity | 
**portfolio_code** | **str** | The portfolio code of the given entity | 
**transaction_id** | **str** | The transaction Id of the PortfolioTransaction being adjusted | 
**nav_activity_adjustment_type** | **str** | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment. | 
## Example

```python
from lusid.models.portfolio_transaction_adjustment import PortfolioTransactionAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav_activity_adjustment_source: StrictStr = "example_nav_activity_adjustment_source"
as_at: datetime = # Replace with your value
portfolio_scope: StrictStr = "example_portfolio_scope"
portfolio_code: StrictStr = "example_portfolio_code"
transaction_id: StrictStr = "example_transaction_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
portfolio_transaction_adjustment_instance = PortfolioTransactionAdjustment(nav_activity_adjustment_source=nav_activity_adjustment_source, as_at=as_at, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, transaction_id=transaction_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

