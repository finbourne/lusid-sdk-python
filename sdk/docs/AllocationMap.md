# AllocationMap

The rules that say which investor records share in the economics of a member of a Fund Structure, and on what basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The display name of the Allocation Map. | 
**description** | **str** | An optional description for the Allocation Map. | [optional] 
**structure_member_id** | [**ResourceId**](ResourceId.md) |  | 
**inherits_from** | [**ResourceId**](ResourceId.md) |  | [optional] 
**participants** | [**AllocationMapParticipants**](AllocationMapParticipants.md) |  | 
**basis_by_event_type** | [**List[AllocationMapEventBasis]**](AllocationMapEventBasis.md) | The basis on which each kind of allocation event is shared between the participants. At most one entry per event type. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.allocation_map import AllocationMap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
structure_member_id: ResourceId = # Replace with your value
inherits_from: Optional[ResourceId] = # Replace with your value
participants: AllocationMapParticipants
basis_by_event_type: List[AllocationMapEventBasis] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
allocation_map_instance = AllocationMap(href=href, id=id, name=name, description=description, structure_member_id=structure_member_id, inherits_from=inherits_from, participants=participants, basis_by_event_type=basis_by_event_type, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

