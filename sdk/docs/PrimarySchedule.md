# PrimarySchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_handler_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.primary_schedule import PrimarySchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_handler_id: ResourceId = # Replace with your value
primary_schedule_instance = PrimarySchedule(event_handler_id=event_handler_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

