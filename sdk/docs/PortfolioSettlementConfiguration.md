# PortfolioSettlementConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_settlement** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
**cash_settlement** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
**deferred_cash_receipt** | [**SettlementConfigurationCategory**](SettlementConfigurationCategory.md) |  | [optional] 
**transaction_matching_alternative_id** | [**TransactionMatchingAlternativeId**](TransactionMatchingAlternativeId.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_settlement_configuration import PortfolioSettlementConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

stock_settlement: Optional[SettlementConfigurationCategory] = # Replace with your value
cash_settlement: Optional[SettlementConfigurationCategory] = # Replace with your value
deferred_cash_receipt: Optional[SettlementConfigurationCategory] = # Replace with your value
transaction_matching_alternative_id: Optional[TransactionMatchingAlternativeId] = # Replace with your value
portfolio_settlement_configuration_instance = PortfolioSettlementConfiguration(stock_settlement=stock_settlement, cash_settlement=cash_settlement, deferred_cash_receipt=deferred_cash_receipt, transaction_matching_alternative_id=transaction_matching_alternative_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

