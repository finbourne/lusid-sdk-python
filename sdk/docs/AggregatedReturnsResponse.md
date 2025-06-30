# AggregatedReturnsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[AggregatedReturn]]** | Aggregated returns grouped by ReturnId | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.aggregated_returns_response import AggregatedReturnsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
results: Optional[Dict[str, conlist(AggregatedReturn)]] = # Replace with your value
links: Optional[conlist(Link)] = None
aggregated_returns_response_instance = AggregatedReturnsResponse(href=href, results=results, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

