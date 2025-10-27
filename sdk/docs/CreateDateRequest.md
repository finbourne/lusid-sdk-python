# CreateDateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_id** | **str** |  | 
**from_utc** | **datetime** |  | 
**to_utc** | **datetime** |  | 
**time_zone** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | [optional] 
**attributes** | [**DateAttributes**](DateAttributes.md) |  | [optional] 
**source_data** | **Dict[str, Optional[str]]** |  | [optional] 
## Example

```python
from lusid.models.create_date_request import CreateDateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

date_id: StrictStr = "example_date_id"
from_utc: datetime = # Replace with your value
to_utc: datetime = # Replace with your value
time_zone: StrictStr = "example_time_zone"
description: StrictStr = "example_description"
type: Optional[StrictStr] = "example_type"
attributes: Optional[DateAttributes] = None
source_data: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
create_date_request_instance = CreateDateRequest(date_id=date_id, from_utc=from_utc, to_utc=to_utc, time_zone=time_zone, description=description, type=type, attributes=attributes, source_data=source_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

