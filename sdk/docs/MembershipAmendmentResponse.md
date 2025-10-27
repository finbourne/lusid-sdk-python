# MembershipAmendmentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data_model_id** | [**ResourceId**](ResourceId.md) |  | 
**entity_type** | **str** | The type of the entity that was added or removed from the Custom Data Model. | 
**entity_unique_id** | **str** | The entity unique identifier of the entity that was added or removed from the Custom Data Model. | 
**operation** | **str** | The operation that was performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;. | 
**entity_display_name** | **str** | The display name of the entity that was added or removed from the Custom Data Model. | 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
## Example

```python
from lusid.models.membership_amendment_response import MembershipAmendmentResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

custom_data_model_id: ResourceId = # Replace with your value
entity_type: StrictStr = "example_entity_type"
entity_unique_id: StrictStr = "example_entity_unique_id"
operation: StrictStr = "example_operation"
entity_display_name: StrictStr = "example_entity_display_name"
data_model_membership: Optional[DataModelMembership] = # Replace with your value
version: Optional[Version] = None
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
membership_amendment_response_instance = MembershipAmendmentResponse(custom_data_model_id=custom_data_model_id, entity_type=entity_type, entity_unique_id=entity_unique_id, operation=operation, entity_display_name=entity_display_name, data_model_membership=data_model_membership, version=version, staged_modifications=staged_modifications)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

