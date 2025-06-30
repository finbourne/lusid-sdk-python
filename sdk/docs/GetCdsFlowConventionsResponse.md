# GetCdsFlowConventionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**CdsFlowConventions**](CdsFlowConventions.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers that did not resolve to a conventions along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_cds_flow_conventions_response import GetCdsFlowConventionsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
value: Optional[CdsFlowConventions] = None
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
get_cds_flow_conventions_response_instance = GetCdsFlowConventionsResponse(href=href, value=value, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

