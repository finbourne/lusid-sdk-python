# SettlementCycle

The settlement cycle for an instrument
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_day_offset** | **int** |  | 
**calendars** | [**List[ResourceId]**](ResourceId.md) |  | 
## Example

```python
from lusid.models.settlement_cycle import SettlementCycle
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conint, conlist

business_day_offset: conint(strict=True, le=2147483647, ge=0) = Field(..., alias="businessDayOffset")
business_day_offset: StrictInt = 42
calendars: conlist(ResourceId) = # Replace with your value
settlement_cycle_instance = SettlementCycle(business_day_offset=business_day_offset, calendars=calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

