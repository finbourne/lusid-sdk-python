# DeleteInstrumentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**as_at** | **datetime** | The as-at datetime at which the instrument was deleted. | 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_instrument_response import DeleteInstrumentResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
as_at: datetime = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[conlist(Link)] = None
delete_instrument_response_instance = DeleteInstrumentResponse(href=href, as_at=as_at, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

