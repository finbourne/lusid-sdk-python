# FundCalendarEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry | 
**display_name** | **str** | The name of the Fund Calendar entry. | 
**description** | **str** | A description for the Fund Calendar entry. | [optional] 
**nav_type_code** | **str** | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. | 
**effective_at** | **datetime** | The effective at of the Calendar Entry. | [optional] 
**as_at** | **datetime** | The asAt datetime for the Calendar Entry. | [optional] 
**entry_type** | **str** | The type of the Fund Calendar Entry. Only &#39;ValuationPoint&#39; currently supported. The available values are: ValuationPointFundCalendarEntry | 
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
## Example

```python
from lusid.models.fund_calendar_entry import FundCalendarEntry
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
from datetime import datetime
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
nav_type_code: StrictStr = "example_nav_type_code"
effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
entry_type: StrictStr = "example_entry_type"
version: Version = # Replace with your value
href: Optional[StrictStr] = "example_href"
fund_calendar_entry_instance = FundCalendarEntry(code=code, display_name=display_name, description=description, nav_type_code=nav_type_code, effective_at=effective_at, as_at=as_at, entry_type=entry_type, version=version, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

