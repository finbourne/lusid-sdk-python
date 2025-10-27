# PagedResourceListOfFundCalendarEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[FundCalendarEntry]**](FundCalendarEntry.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.paged_resource_list_of_fund_calendar_entry import PagedResourceListOfFundCalendarEntry
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
values: List[FundCalendarEntry]
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
paged_resource_list_of_fund_calendar_entry_instance = PagedResourceListOfFundCalendarEntry(next_page=next_page, previous_page=previous_page, values=values, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

