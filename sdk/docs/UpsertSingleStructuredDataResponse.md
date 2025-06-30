# UpsertSingleStructuredDataResponse

Response from upserting structured data document
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | **datetime** | The value that was successfully retrieved. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
value: Optional[datetime] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_single_structured_data_response_instance = UpsertSingleStructuredDataResponse(href=href, value=value, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

