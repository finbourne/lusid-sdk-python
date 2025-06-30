# ResourceListOfProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ModelProperty]**](ModelProperty.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
## Example

```python
from lusid.models.resource_list_of_property import ResourceListOfProperty
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

values: conlist(ModelProperty) = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
resource_list_of_property_instance = ResourceListOfProperty(values=values, href=href, links=links, next_page=next_page, previous_page=previous_page)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

