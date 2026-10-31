# ChargeableGainsTakeOnAddition

One acquisition added to a taken-on 1982 holding since 31 March 1982, carried as its own record inside the holding
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**cost** | **float** |  | 
**indexation** | **float** |  | 
**paid_cost** | **float** |  | [optional] 
## Example

```python
from lusid.models.chargeable_gains_take_on_addition import ChargeableGainsTakeOnAddition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
cost: Union[StrictFloat, StrictInt]
indexation: Union[StrictFloat, StrictInt]
paid_cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
chargeable_gains_take_on_addition_instance = ChargeableGainsTakeOnAddition(var_date=var_date, cost=cost, indexation=indexation, paid_cost=paid_cost)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

