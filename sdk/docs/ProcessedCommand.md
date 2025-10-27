# ProcessedCommand

The list of commands.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the command issued. | 
**path** | **str** | The unique identifier for the command including the request id. | [optional] 
**user_id** | [**User**](User.md) |  | 
**processed_time** | **datetime** | The asAt datetime that the events published by the processing of this command were committed to LUSID. | 
## Example

```python
from lusid.models.processed_command import ProcessedCommand
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

description: StrictStr = "example_description"
path: Optional[StrictStr] = "example_path"
user_id: User = # Replace with your value
processed_time: datetime = # Replace with your value
processed_command_instance = ProcessedCommand(description=description, path=path, user_id=user_id, processed_time=processed_time)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

