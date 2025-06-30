# AnnulQuotesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **Dict[str, datetime]** | The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be deleted along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.annul_quotes_response import AnnulQuotesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, datetime]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
annul_quotes_response_instance = AnnulQuotesResponse(href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

