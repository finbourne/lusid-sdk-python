# DeleteInstrumentPropertiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The as-at datetime at which properties were deleted. | 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_instrument_properties_response import DeleteInstrumentPropertiesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
as_at: datetime = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[conlist(Link)] = None
delete_instrument_properties_response_instance = DeleteInstrumentPropertiesResponse(as_at=as_at, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

