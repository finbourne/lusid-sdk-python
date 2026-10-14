# ProcessingGroupNextScheduledDetails

The next scheduled occurrence of a Processing Group: the next execution date after the requested date,  together with the executed (resolved) contents of the reference list the Processing Group operates over.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_schedule_date** | **datetime** | The next execution date strictly after the requested date. | [optional] 
**resolved_reference_list** | [**ReferenceList**](ReferenceList.md) |  | [optional] 
## Example

```python
from lusid.models.processing_group_next_scheduled_details import ProcessingGroupNextScheduledDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

next_schedule_date: Optional[datetime] = # Replace with your value
resolved_reference_list: Optional[ReferenceList] = # Replace with your value
processing_group_next_scheduled_details_instance = ProcessingGroupNextScheduledDetails(next_schedule_date=next_schedule_date, resolved_reference_list=resolved_reference_list)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

