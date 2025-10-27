# DeletedEntityResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effective_from** | **datetime** | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the deletion was committed to LUSID. | 
**entity_type** | **str** | The type of the entity that the deleted response applies to. | [optional] 
**entity_unique_id** | **str** | The unique Id of the entity that the deleted response applies to. | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.deleted_entity_response import DeletedEntityResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
effective_from: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
entity_type: Optional[StrictStr] = "example_entity_type"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[List[Link]] = None
deleted_entity_response_instance = DeletedEntityResponse(href=href, effective_from=effective_from, as_at=as_at, entity_type=entity_type, entity_unique_id=entity_unique_id, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

