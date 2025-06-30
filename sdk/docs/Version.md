# Version

The version metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** | The effective datetime at which this version became valid. Only applies when a single entity is being interacted with. | 
**as_at_date** | **datetime** | The asAt datetime at which the data was committed to LUSID. | 
**as_at_created** | **datetime** | The asAt datetime at which the entity was first created in LUSID. | [optional] 
**user_id_created** | **str** | The unique id of the user who created the entity. | [optional] 
**request_id_created** | **str** | The unique request id of the command that created the entity. | [optional] 
**reason_created** | **str** | The reason for an entity creation. | [optional] 
**as_at_modified** | **datetime** | The asAt datetime at which the entity (including its properties) was last updated in LUSID. | [optional] 
**user_id_modified** | **str** | The unique id of the user who last updated the entity (including its properties) in LUSID. | [optional] 
**request_id_modified** | **str** | The unique request id of the command that last updated the entity (including its properties) in LUSID. | [optional] 
**reason_modified** | **str** | The reason for an entity modification. | [optional] 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**entity_unique_id** | **str** | The unique id of the entity | [optional] 
**staged_modification_id_modified** | **str** | The ID of the staged change that resulted in the most recent modification. | [optional] 
## Example

```python
from lusid.models.version import Version
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
from datetime import datetime
effective_from: datetime = # Replace with your value
as_at_date: datetime = # Replace with your value
as_at_created: Optional[datetime] = # Replace with your value
user_id_created: Optional[StrictStr] = "example_user_id_created"
request_id_created: Optional[StrictStr] = "example_request_id_created"
reason_created: Optional[StrictStr] = "example_reason_created"
as_at_modified: Optional[datetime] = # Replace with your value
user_id_modified: Optional[StrictStr] = "example_user_id_modified"
request_id_modified: Optional[StrictStr] = "example_request_id_modified"
reason_modified: Optional[StrictStr] = "example_reason_modified"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
staged_modification_id_modified: Optional[StrictStr] = "example_staged_modification_id_modified"
version_instance = Version(effective_from=effective_from, as_at_date=as_at_date, as_at_created=as_at_created, user_id_created=user_id_created, request_id_created=request_id_created, reason_created=reason_created, as_at_modified=as_at_modified, user_id_modified=user_id_modified, request_id_modified=request_id_modified, reason_modified=reason_modified, as_at_version_number=as_at_version_number, entity_unique_id=entity_unique_id, staged_modification_id_modified=staged_modification_id_modified)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

