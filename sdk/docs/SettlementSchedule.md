# SettlementSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **str** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**units** | **float** |  | [optional] 
**bond_interest** | **float** |  | [optional] 
**movement_name** | **str** |  | [optional] 
**movement_type** | **str** |  | [optional] 
**unsettled_units** | **float** |  | [optional] 
**overdue_units** | **float** |  | [optional] 
## Example

```python
from lusid.models.settlement_schedule import SettlementSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trade_id: Optional[StrictStr] = "example_trade_id"
settlement_date: Optional[datetime] = # Replace with your value
units: Optional[Union[StrictFloat, StrictInt]] = None
bond_interest: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
movement_name: Optional[StrictStr] = "example_movement_name"
movement_type: Optional[StrictStr] = "example_movement_type"
unsettled_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
overdue_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_schedule_instance = SettlementSchedule(trade_id=trade_id, settlement_date=settlement_date, units=units, bond_interest=bond_interest, movement_name=movement_name, movement_type=movement_type, unsettled_units=unsettled_units, overdue_units=overdue_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

