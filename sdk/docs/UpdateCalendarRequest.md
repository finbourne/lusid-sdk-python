# UpdateCalendarRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weekend_mask** | [**WeekendMask**](WeekendMask.md) |  | 
**source_provider** | **str** |  | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) |  | 
## Example

```python
from lusid.models.update_calendar_request import UpdateCalendarRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

weekend_mask: WeekendMask = # Replace with your value
source_provider: StrictStr = "example_source_provider"
properties: conlist(ModelProperty) = # Replace with your value
update_calendar_request_instance = UpdateCalendarRequest(weekend_mask=weekend_mask, source_provider=source_provider, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

