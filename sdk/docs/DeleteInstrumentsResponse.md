# DeleteInstrumentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**as_at** | **datetime** | The as-at datetime at which the instrument was deleted. | 
**staged** | [**Dict[str, StagedModificationsInfo]**](StagedModificationsInfo.md) | Information about the pending staged modifications for the current entity. | [optional] [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_instruments_response import DeleteInstrumentsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
as_at: datetime = # Replace with your value
staged: Optional[Dict[str, StagedModificationsInfo]] = # Replace with your value
links: Optional[conlist(Link)] = None
delete_instruments_response_instance = DeleteInstrumentsResponse(href=href, as_at=as_at, staged=staged, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

