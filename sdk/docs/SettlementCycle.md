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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

business_day_offset: StrictInt = # Replace with your value
business_day_offset: StrictInt = 42
calendars: List[ResourceId]
settlement_cycle_instance = SettlementCycle(business_day_offset=business_day_offset, calendars=calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

