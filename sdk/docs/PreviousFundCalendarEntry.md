# PreviousFundCalendarEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry | 
**display_name** | **str** | The name of the Fund Calendar entry. | 
**description** | **str** | A description for the Fund Calendar entry. | [optional] 
**effective_at** | **datetime** | The effective at of the Calendar Entry. | [optional] 
**as_at** | **datetime** | The asAt datetime for the Calendar Entry. | 
## Example

```python
from lusid.models.previous_fund_calendar_entry import PreviousFundCalendarEntry
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from datetime import datetime
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
effective_at: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
previous_fund_calendar_entry_instance = PreviousFundCalendarEntry(code=code, display_name=display_name, description=description, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

