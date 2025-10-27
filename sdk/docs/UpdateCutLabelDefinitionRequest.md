# UpdateCutLabelDefinitionRequest

This request specifies a new Cut Label Definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
**cut_local_time** | [**CutLocalTime**](CutLocalTime.md) |  | 
**time_zone** | **str** |  | 
## Example

```python
from lusid.models.update_cut_label_definition_request import UpdateCutLabelDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
cut_local_time: CutLocalTime = # Replace with your value
time_zone: StrictStr = "example_time_zone"
update_cut_label_definition_request_instance = UpdateCutLabelDefinitionRequest(display_name=display_name, description=description, cut_local_time=cut_local_time, time_zone=time_zone)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

