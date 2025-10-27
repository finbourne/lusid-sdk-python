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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: datetime = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[List[Link]] = None
delete_instrument_properties_response_instance = DeleteInstrumentPropertiesResponse(as_at=as_at, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

