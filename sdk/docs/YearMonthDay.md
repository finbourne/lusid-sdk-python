# YearMonthDay

A date in component form.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | The year of the date. | 
**month** | **int** | The month of the date. | 
**day** | **int** | The day in month of the date. | 
## Example

```python
from lusid.models.year_month_day import YearMonthDay
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

year: StrictInt = # Replace with your value
year: StrictInt = 42
month: StrictInt = # Replace with your value
month: StrictInt = 42
day: StrictInt = # Replace with your value
day: StrictInt = 42
year_month_day_instance = YearMonthDay(year=year, month=month, day=day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

