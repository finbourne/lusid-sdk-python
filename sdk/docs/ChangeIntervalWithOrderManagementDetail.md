# ChangeIntervalWithOrderManagementDetail

Defines a change that occured for an entity, with extra detail about the change
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **Dict[str, Optional[str]]** | Information about the particular instance of the ChangeInterval (supplied information depends on the type of Action). Contains extra detail for order management actions such as related entity ids and compliance run details. | [optional] 
**action_description** | **str** | Description of the action performed on the entity. | [optional] 
**as_at_modified** | **datetime** | The date/time of the change. | [optional] 
**user_id_modified** | **str** | The unique identifier of the user that made the change. | [optional] 
**request_id_modified** | **str** | The unique identifier of the request that the changes were part of. | [optional] 
**reason_modified** | **str** | The reason for an entity modification. | [optional] 
**as_at_version_number** | **int** | The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself. | [optional] 
**staged_modification_id_modified** | **str** | The id of the staged modification that was approved. Will be null if the change didn&#39;t come from a staged modification. | [optional] 
**action** | **str** | The action performed on the field. | [optional] 
**attribute_name** | **str** | The name of the field or property that has been changed. | [optional] 
**previous_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**new_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effective_range** | [**EffectiveRange**](EffectiveRange.md) |  | [optional] 
## Example

```python
from lusid.models.change_interval_with_order_management_detail import ChangeIntervalWithOrderManagementDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

detail: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
action_description: Optional[StrictStr] = "example_action_description"
as_at_modified: Optional[datetime] = # Replace with your value
user_id_modified: Optional[StrictStr] = "example_user_id_modified"
request_id_modified: Optional[StrictStr] = "example_request_id_modified"
reason_modified: Optional[StrictStr] = "example_reason_modified"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
staged_modification_id_modified: Optional[StrictStr] = "example_staged_modification_id_modified"
action: Optional[StrictStr] = "example_action"
attribute_name: Optional[StrictStr] = "example_attribute_name"
previous_value: Optional[PropertyValue] = # Replace with your value
new_value: Optional[PropertyValue] = # Replace with your value
effective_range: Optional[EffectiveRange] = # Replace with your value
change_interval_with_order_management_detail_instance = ChangeIntervalWithOrderManagementDetail(detail=detail, action_description=action_description, as_at_modified=as_at_modified, user_id_modified=user_id_modified, request_id_modified=request_id_modified, reason_modified=reason_modified, as_at_version_number=as_at_version_number, staged_modification_id_modified=staged_modification_id_modified, action=action, attribute_name=attribute_name, previous_value=previous_value, new_value=new_value, effective_range=effective_range)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

