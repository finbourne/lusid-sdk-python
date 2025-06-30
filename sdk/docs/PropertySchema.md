# PropertySchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**values** | [**Dict[str, FieldSchema]**](FieldSchema.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.property_schema import PropertySchema
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, FieldSchema]] = None
links: Optional[conlist(Link)] = None
property_schema_instance = PropertySchema(href=href, values=values, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

