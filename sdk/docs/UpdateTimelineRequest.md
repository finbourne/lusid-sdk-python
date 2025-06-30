# UpdateTimelineRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Timeline. | 
**description** | **str** | A description for the Timeline. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Timelines properties. These will be from the &#39;Timeline&#39; domain. | [optional] 
## Example

```python
from lusid.models.update_timeline_request import UpdateTimelineRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
update_timeline_request_instance = UpdateTimelineRequest(display_name=display_name, description=description, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

