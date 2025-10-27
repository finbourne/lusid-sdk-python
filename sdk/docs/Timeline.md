# Timeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The name of the Timeline. | [optional] 
**description** | **str** | A description for the Timeline. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Timelines properties. These will be from the &#39;Timeline&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.timeline import Timeline
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
timeline_instance = Timeline(id=id, display_name=display_name, description=description, properties=properties, version=version, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

