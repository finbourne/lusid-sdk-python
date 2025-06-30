# PeriodDiaryEntriesReopenedResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effective_from** | **datetime** | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the deletion was committed to LUSID. | 
**period_diary_entries_removed** | **int** | Number of Diary Entries removed as a result of reopening periods | 
**period_diary_entries_from** | **datetime** | The start point where periods were removed from | 
**period_diary_entries_to** | **datetime** | The end point where periods were removed to | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.period_diary_entries_reopened_response import PeriodDiaryEntriesReopenedResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
effective_from: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
period_diary_entries_removed: StrictInt = # Replace with your value
period_diary_entries_removed: StrictInt = 42
period_diary_entries_from: datetime = # Replace with your value
period_diary_entries_to: datetime = # Replace with your value
links: Optional[conlist(Link)] = None
period_diary_entries_reopened_response_instance = PeriodDiaryEntriesReopenedResponse(href=href, effective_from=effective_from, as_at=as_at, period_diary_entries_removed=period_diary_entries_removed, period_diary_entries_from=period_diary_entries_from, period_diary_entries_to=period_diary_entries_to, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

