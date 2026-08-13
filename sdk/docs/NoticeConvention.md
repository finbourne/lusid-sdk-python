# NoticeConvention

Defines the notice period by which a cancellation election must be made ahead of the  cancel effective date, else the option lapses.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | **List[str]** | Holiday calendar code(s) used to resolve business days, required when the day type is Business. | [optional] 
**day_type** | **str** | Indicates whether the notice days are counted using business days or calendar days.                Supported string (enumeration) values are: [Business, Calendar]. Available values: Business, Calendar. | 
**notice_days** | **int** | The number of days prior to the cancel effective date by which the election must be made.                Defaults to 2 if not set. | [optional] [default to 2]
## Example

```python
from lusid.models.notice_convention import NoticeConvention
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calendars: Optional[List[StrictStr]] = # Replace with your value
day_type: StrictStr = "example_day_type"
notice_days: Optional[StrictInt] = # Replace with your value
notice_days: Optional[StrictInt] = None
notice_convention_instance = NoticeConvention(calendars=calendars, day_type=day_type, notice_days=notice_days)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

