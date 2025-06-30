# CompositeBreakdownResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[CompositeBreakdown]]** | The Composite calculation with the constituens which were included. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.composite_breakdown_response import CompositeBreakdownResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
results: Dict[str, conlist(CompositeBreakdown)] = # Replace with your value
links: Optional[conlist(Link)] = None
composite_breakdown_response_instance = CompositeBreakdownResponse(href=href, results=results, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

