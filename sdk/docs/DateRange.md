# DateRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** |  | 
**until_date** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.date_range import DateRange
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
from_date: datetime = # Replace with your value
until_date: Optional[datetime] = # Replace with your value
date_range_instance = DateRange(from_date=from_date, until_date=until_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

