# Calendar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** |  | 
**weekend_mask** | [**WeekendMask**](WeekendMask.md) |  | 
**source_provider** | **str** |  | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.calendar import Calendar
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
type: StrictStr = "example_type"
weekend_mask: WeekendMask = # Replace with your value
source_provider: StrictStr = "example_source_provider"
properties: List[ModelProperty]
version: Optional[Version] = None
links: Optional[List[Link]] = None
calendar_instance = Calendar(href=href, id=id, type=type, weekend_mask=weekend_mask, source_provider=source_provider, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

