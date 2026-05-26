# NavSettlementConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_settlement** | [**NavSettlementConfigurationCategory**](NavSettlementConfigurationCategory.md) |  | [optional] 
**deferred_cash_receipt** | [**NavSettlementConfigurationCategory**](NavSettlementConfigurationCategory.md) |  | [optional] 
## Example

```python
from lusid.models.nav_settlement_configuration import NavSettlementConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cash_settlement: Optional[NavSettlementConfigurationCategory] = # Replace with your value
deferred_cash_receipt: Optional[NavSettlementConfigurationCategory] = # Replace with your value
nav_settlement_configuration_instance = NavSettlementConfiguration(cash_settlement=cash_settlement, deferred_cash_receipt=deferred_cash_receipt)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

