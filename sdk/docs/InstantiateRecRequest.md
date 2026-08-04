# InstantiateRecRequest

The request to instantiate a new rec instance from a rec definition and start its first run. Each  date accepts a date-time or a LUSID cut label, and defaults to the current date-time when omitted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**left_effective_at** | **str** | The left effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. | [optional] 
**left_as_at** | **str** | The left asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. | [optional] 
**right_effective_at** | **str** | The right effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. | [optional] 
**right_as_at** | **str** | The right asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. | [optional] 
## Example

```python
from lusid.models.instantiate_rec_request import InstantiateRecRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_definition_id: ResourceId = # Replace with your value
left_effective_at: Optional[StrictStr] = "example_left_effective_at"
left_as_at: Optional[StrictStr] = "example_left_as_at"
right_effective_at: Optional[StrictStr] = "example_right_effective_at"
right_as_at: Optional[StrictStr] = "example_right_as_at"
instantiate_rec_request_instance = InstantiateRecRequest(rec_definition_id=rec_definition_id, left_effective_at=left_effective_at, left_as_at=left_as_at, right_effective_at=right_effective_at, right_as_at=right_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

