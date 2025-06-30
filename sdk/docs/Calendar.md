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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
weekend_mask: WeekendMask = # Replace with your value
source_provider: StrictStr = "example_source_provider"
properties: conlist(ModelProperty) = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
calendar_instance = Calendar(href=href, id=id, type=type, weekend_mask=weekend_mask, source_provider=source_provider, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

