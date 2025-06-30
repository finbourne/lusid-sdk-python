# UpsertCustomEntitiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CustomEntityResponse]**](CustomEntityResponse.md) | The custom-entities which have been successfully updated or created. | [optional] 
**staged** | [**Dict[str, CustomEntityResponse]**](CustomEntityResponse.md) | The custom-entities that have been staged for update or creation. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The custom-entities that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_custom_entities_response import UpsertCustomEntitiesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, CustomEntityResponse]] = # Replace with your value
staged: Optional[Dict[str, CustomEntityResponse]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_custom_entities_response_instance = UpsertCustomEntitiesResponse(href=href, values=values, staged=staged, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

