# CompositeDispersionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[CompositeDispersion]]** | Dispersion returns calculation grouped by ReturnId | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.composite_dispersion_response import CompositeDispersionResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
results: Optional[Dict[str, conlist(CompositeDispersion)]] = # Replace with your value
links: Optional[conlist(Link)] = None
composite_dispersion_response_instance = CompositeDispersionResponse(href=href, results=results, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

