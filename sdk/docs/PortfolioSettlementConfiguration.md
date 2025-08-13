# PortfolioSettlementConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_settlement** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
**cash_settlement** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
**deferred_cash_receipt** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_settlement_configuration import PortfolioSettlementConfiguration
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

stock_settlement: Optional[SettlementConfigurationCategory] = # Replace with your value
cash_settlement: Optional[SettlementConfigurationCategory] = # Replace with your value
deferred_cash_receipt: Optional[SettlementConfigurationCategory] = # Replace with your value
portfolio_settlement_configuration_instance = PortfolioSettlementConfiguration(stock_settlement=stock_settlement, cash_settlement=cash_settlement, deferred_cash_receipt=deferred_cash_receipt)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

