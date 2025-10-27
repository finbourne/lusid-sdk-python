# DayMonth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | Day part of Day, Month for Year End date specification. | 
**month** | **int** | Month part of Day, Month for Year End date specification. | 
## Example

```python
from lusid.models.day_month import DayMonth
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

day: StrictInt = # Replace with your value
day: StrictInt = 42
month: StrictInt = # Replace with your value
month: StrictInt = 42
day_month_instance = DayMonth(day=day, month=month)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

