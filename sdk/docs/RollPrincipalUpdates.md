# RollPrincipalUpdates

Describes changes to the principal on a FlexibleDeposit instrument as the result of a DepositRollEvent.  Either the principal to be withdrawn or the principal increase must be specified (either as an amount or a percentage).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdraw_principal_amount** | **float** | The amount of principal that should be withdrawn from the FlexibleDeposit. | [optional] 
**withdraw_principal_percentage** | **float** | The percentage of principal that should be withdrawn from the FlexibleDeposit. | [optional] 
**increase_principal_amount** | **float** | The amount of principal that should be added to the FlexibleDeposit. | [optional] 
**increase_principal_percentage** | **float** | The percentage of principal that should be added to the FlexibleDeposit. | [optional] 
## Example

```python
from lusid.models.roll_principal_updates import RollPrincipalUpdates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

withdraw_principal_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
withdraw_principal_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
increase_principal_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
increase_principal_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
roll_principal_updates_instance = RollPrincipalUpdates(withdraw_principal_amount=withdraw_principal_amount, withdraw_principal_percentage=withdraw_principal_percentage, increase_principal_amount=increase_principal_amount, increase_principal_percentage=increase_principal_percentage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

