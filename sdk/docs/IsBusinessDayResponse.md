# IsBusinessDayResponse

Whether or not a DateTimeOffset is a business DateTime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_date_time** | **datetime** |  | 
**is_business_day** | **bool** |  | 
## Example

```python
from lusid.models.is_business_day_response import IsBusinessDayResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictBool
from datetime import datetime
requested_date_time: datetime = # Replace with your value
is_business_day: StrictBool = # Replace with your value
is_business_day:StrictBool = True
is_business_day_response_instance = IsBusinessDayResponse(requested_date_time=requested_date_time, is_business_day=is_business_day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

