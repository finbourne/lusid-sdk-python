# UpsertReturnsResponse

Response from upserting Returns
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **List[Dict[str, datetime]]** | The set of values that were successfully retrieved. | [optional] 
**failed** | **List[Dict[str, ErrorDetail]]** | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_returns_response import UpsertReturnsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
version: Version = # Replace with your value
href: Optional[StrictStr] = "example_href"
values: Optional[conlist(Dict[str, datetime])] = # Replace with your value
failed: Optional[conlist(Dict[str, ErrorDetail])] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_returns_response_instance = UpsertReturnsResponse(version=version, href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

