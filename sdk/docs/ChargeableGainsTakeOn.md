# ChargeableGainsTakeOn

Carried-forward chargeable-gains balances for a tax-lot taken on under the UK chargeable gains accounting method
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Available values: Section104Pool, Holding1982, Holding1965. | 
**indexation** | **float** |  | [optional] 
**indexed_to** | **datetime** |  | [optional] 
**original_cost** | **float** |  | [optional] 
**market_value1982** | **float** |  | [optional] 
**rebasing_election** | **bool** |  | [optional] 
## Example

```python
from lusid.models.chargeable_gains_take_on import ChargeableGainsTakeOn
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

role: StrictStr = "example_role"
indexation: Optional[Union[StrictFloat, StrictInt]] = None
indexed_to: Optional[datetime] = # Replace with your value
original_cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
market_value1982: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rebasing_election: Optional[StrictBool] = # Replace with your value
rebasing_election:Optional[StrictBool] = None
chargeable_gains_take_on_instance = ChargeableGainsTakeOn(role=role, indexation=indexation, indexed_to=indexed_to, original_cost=original_cost, market_value1982=market_value1982, rebasing_election=rebasing_election)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

