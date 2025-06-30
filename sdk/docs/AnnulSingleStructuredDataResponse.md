# AnnulSingleStructuredDataResponse

The response to a request to annul (delete) a set of structured data from Lusid. This might have been for market data or some other structured entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | **datetime** | The time at which the identifier was annulled | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
value: Optional[datetime] = # Replace with your value
links: Optional[conlist(Link)] = None
annul_single_structured_data_response_instance = AnnulSingleStructuredDataResponse(href=href, value=value, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

