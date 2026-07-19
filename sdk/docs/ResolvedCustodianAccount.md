# ResolvedCustodianAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_selector** | **str** | Available values: From, To. | [optional] 
**custodian_account** | [**CustodianAccount**](CustodianAccount.md) |  | 
**resolution_type** | **str** | Available values: BookingEntry, ContextCustodian, RelatedAccount, PortfolioDefault. | 
## Example

```python
from lusid.models.resolved_custodian_account import ResolvedCustodianAccount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

account_selector: Optional[StrictStr] = "example_account_selector"
custodian_account: CustodianAccount = # Replace with your value
resolution_type: StrictStr = "example_resolution_type"
resolved_custodian_account_instance = ResolvedCustodianAccount(account_selector=account_selector, custodian_account=custodian_account, resolution_type=resolution_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

