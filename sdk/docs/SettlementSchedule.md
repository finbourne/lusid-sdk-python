# SettlementSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **str** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**units** | **float** |  | [optional] 
## Example

```python
from lusid.models.settlement_schedule import SettlementSchedule
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from datetime import datetime
trade_id: Optional[StrictStr] = "example_trade_id"
settlement_date: Optional[datetime] = # Replace with your value
units: Optional[Union[StrictFloat, StrictInt]] = None
settlement_schedule_instance = SettlementSchedule(trade_id=trade_id, settlement_date=settlement_date, units=units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

