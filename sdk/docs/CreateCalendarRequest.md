# CreateCalendarRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | [**ResourceId**](ResourceId.md) |  | 
**calendar_type** | **str** |  | 
**weekend_mask** | [**WeekendMask**](WeekendMask.md) |  | 
**source_provider** | **str** |  | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) |  | [optional] 
## Example

```python
from lusid.models.create_calendar_request import CreateCalendarRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

calendar_id: ResourceId = # Replace with your value
calendar_type: StrictStr = "example_calendar_type"
weekend_mask: WeekendMask = # Replace with your value
source_provider: StrictStr = "example_source_provider"
properties: Optional[conlist(ModelProperty)] = None
create_calendar_request_instance = CreateCalendarRequest(calendar_id=calendar_id, calendar_type=calendar_type, weekend_mask=weekend_mask, source_provider=source_provider, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

