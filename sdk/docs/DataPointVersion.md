# DataPointVersion

The version metadata for DataPoints.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_created** | **datetime** | The asAt datetime at which the entity was first created in LUSID. | [optional] 
**user_id_created** | **str** | The unique id of the user who created the entity. | [optional] 
**request_id_created** | **str** | The unique request id of the command that created the entity. | [optional] 
**as_at_modified** | **datetime** | The asAt datetime at which the entity (including its properties) was last updated in LUSID. | [optional] 
**user_id_modified** | **str** | The unique id of the user who last updated the entity (including its properties) in LUSID. | [optional] 
**request_id_modified** | **str** | The unique request id of the command that last updated the entity (including its properties) in LUSID. | [optional] 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] 
**entity_unique_id** | **str** | The unique id of the entity | [optional] 
## Example

```python
from lusid.models.data_point_version import DataPointVersion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_created: Optional[datetime] = # Replace with your value
user_id_created: Optional[StrictStr] = "example_user_id_created"
request_id_created: Optional[StrictStr] = "example_request_id_created"
as_at_modified: Optional[datetime] = # Replace with your value
user_id_modified: Optional[StrictStr] = "example_user_id_modified"
request_id_modified: Optional[StrictStr] = "example_request_id_modified"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
data_point_version_instance = DataPointVersion(as_at_created=as_at_created, user_id_created=user_id_created, request_id_created=request_id_created, as_at_modified=as_at_modified, user_id_modified=user_id_modified, request_id_modified=request_id_modified, as_at_version_number=as_at_version_number, entity_unique_id=entity_unique_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

