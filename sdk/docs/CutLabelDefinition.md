# CutLabelDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cut_local_time** | [**CutLocalTime**](CutLocalTime.md) |  | [optional] 
**time_zone** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cut_label_definition import CutLabelDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
cut_local_time: Optional[CutLocalTime] = # Replace with your value
time_zone: Optional[StrictStr] = "example_time_zone"
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
cut_label_definition_instance = CutLabelDefinition(code=code, display_name=display_name, description=description, cut_local_time=cut_local_time, time_zone=time_zone, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

