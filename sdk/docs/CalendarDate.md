# CalendarDate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**date_identifier** | **str** |  | 
**from_utc** | **datetime** |  | 
**to_utc** | **datetime** |  | 
**local_date** | **str** |  | 
**timezone** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | [optional] 
**attributes** | [**DateAttributes**](DateAttributes.md) |  | [optional] 
**source_data** | **Dict[str, Optional[str]]** |  | [optional] 
## Example

```python
from lusid.models.calendar_date import CalendarDate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
date_identifier: StrictStr = "example_date_identifier"
from_utc: datetime = # Replace with your value
to_utc: datetime = # Replace with your value
local_date: StrictStr = "example_local_date"
timezone: StrictStr = "example_timezone"
description: StrictStr = "example_description"
type: Optional[StrictStr] = "example_type"
attributes: Optional[DateAttributes] = None
source_data: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
calendar_date_instance = CalendarDate(href=href, date_identifier=date_identifier, from_utc=from_utc, to_utc=to_utc, local_date=local_date, timezone=timezone, description=description, type=type, attributes=attributes, source_data=source_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

