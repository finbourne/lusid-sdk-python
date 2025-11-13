# RollInterestUpdates

Describes changes to the interest of a FlexibleDeposit instrument as the result of a DepositRollEvent.  Both the interest to be withdrawn and the interest to be reinvested must be specified (either as an amount or as a percentage).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdraw_interest_amount** | **float** | The amount of interest that should be withdrawn from a FlexibleDeposit as the result of a roll event. | [optional] 
**withdraw_interest_percentage** | **float** | The percentage of interest that should be withdrawn from a FlexibleDeposit instrument as the result of a roll event. | [optional] 
**reinvest_interest_amount** | **float** | The amount of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event. | [optional] 
**reinvest_interest_percentage** | **float** | The percentage of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event. | [optional] 
## Example

```python
from lusid.models.roll_interest_updates import RollInterestUpdates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

withdraw_interest_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
withdraw_interest_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reinvest_interest_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reinvest_interest_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
roll_interest_updates_instance = RollInterestUpdates(withdraw_interest_amount=withdraw_interest_amount, withdraw_interest_percentage=withdraw_interest_percentage, reinvest_interest_amount=reinvest_interest_amount, reinvest_interest_percentage=reinvest_interest_percentage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

