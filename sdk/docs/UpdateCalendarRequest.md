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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

weekend_mask: WeekendMask = # Replace with your value
source_provider: StrictStr = "example_source_provider"
properties: List[ModelProperty]
update_calendar_request_instance = UpdateCalendarRequest(weekend_mask=weekend_mask, source_provider=source_provider, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

