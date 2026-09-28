# AllocationMapRequest

The request used to create or update an Allocation Map.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Allocation Map. | 
**name** | **str** | The display name of the Allocation Map. | 
**description** | **str** | An optional description for the Allocation Map. | [optional] 
**structure_member_id** | [**ResourceId**](ResourceId.md) |  | 
**inherits_from** | [**ResourceId**](ResourceId.md) |  | [optional] 
**participants** | [**AllocationMapParticipants**](AllocationMapParticipants.md) |  | [optional] 
**basis_by_event_type** | [**List[AllocationMapEventBasis]**](AllocationMapEventBasis.md) | The basis on which each kind of allocation event is shared between the participants. At most one entry per event type. | [optional] 
**effective_at** | **datetime** | The effective datetime from which the Allocation Map applies. Defaults to the beginning of time if not specified, so that the map is visible at every effective datetime. | [optional] 
## Example

```python
from lusid.models.allocation_map_request import AllocationMapRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
structure_member_id: ResourceId = # Replace with your value
inherits_from: Optional[ResourceId] = # Replace with your value
participants: Optional[AllocationMapParticipants] = None
basis_by_event_type: Optional[List[AllocationMapEventBasis]] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
allocation_map_request_instance = AllocationMapRequest(code=code, name=name, description=description, structure_member_id=structure_member_id, inherits_from=inherits_from, participants=participants, basis_by_event_type=basis_by_event_type, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

