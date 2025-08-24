# EventDateRange

A standard representation of the effective date range for the event, used for display, filtering and windowing use cases.  The start and end values for the eventDateRange are mapped from the particular dates contained within the specific  InstrumentEvent schema.  Note that the start and end values may be identical for some types of events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.event_date_range import EventDateRange
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel
from datetime import datetime
start: Optional[datetime] = None
end: Optional[datetime] = None
event_date_range_instance = EventDateRange(start=start, end=end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

