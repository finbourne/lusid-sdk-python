# BatchUpsertDatesForCalendarResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, CalendarDate]**](CalendarDate.md) | The dates which have been successfully upserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The dates that could not be upserted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to the upserted dates | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_dates_for_calendar_response import BatchUpsertDatesForCalendarResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

values: Optional[Dict[str, CalendarDate]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
batch_upsert_dates_for_calendar_response_instance = BatchUpsertDatesForCalendarResponse(values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

