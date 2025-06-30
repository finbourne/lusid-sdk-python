# StagedModification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Id for the staged modification | [optional] 
**as_at_staged** | **datetime** | Time at which the modification was staged. | [optional] 
**user_id_staged** | **str** | Id of the user who created the stage modification request. | [optional] 
**requested_id_staged** | **str** | The Request Id that initiated this staged modification. | [optional] 
**request_reason** | **str** | Reason staged change request made. | [optional] 
**action** | **str** | Type of action of the staged modification, either create, update or delete. | [optional] 
**staging_rule** | [**StagedModificationStagingRule**](StagedModificationStagingRule.md) |  | [optional] 
**decisions** | [**List[StagedModificationDecision]**](StagedModificationDecision.md) | Object containing information relating to the decision on the staged modification. | [optional] 
**decisions_count** | **int** | Number of decisions made. | [optional] 
**status** | **str** | The status of the staged modification. | [optional] 
**as_at_closed** | **datetime** | Time at which the modification was closed by either rejection or approval. | [optional] 
**entity_type** | **str** | The type of the entity that the staged modification applies to. | [optional] 
**scope** | **str** | The scope of the entity that this staged modification applies to. | [optional] 
**entity_unique_id** | **str** | The unique Id of the entity the staged modification applies to. | [optional] 
**requested_changes** | [**RequestedChanges**](RequestedChanges.md) |  | [optional] 
**entity_hrefs** | [**StagedModificationsEntityHrefs**](StagedModificationsEntityHrefs.md) |  | [optional] 
**display_name** | **str** | The display name of the entity the staged modification applies to. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.staged_modification import StagedModification
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
id: Optional[StrictStr] = "example_id"
as_at_staged: Optional[datetime] = # Replace with your value
user_id_staged: Optional[StrictStr] = "example_user_id_staged"
requested_id_staged: Optional[StrictStr] = "example_requested_id_staged"
request_reason: Optional[StrictStr] = "example_request_reason"
action: Optional[StrictStr] = "example_action"
staging_rule: Optional[StagedModificationStagingRule] = # Replace with your value
decisions: Optional[conlist(StagedModificationDecision)] = # Replace with your value
decisions_count: Optional[StrictInt] = # Replace with your value
decisions_count: Optional[StrictInt] = None
status: Optional[StrictStr] = "example_status"
as_at_closed: Optional[datetime] = # Replace with your value
entity_type: Optional[StrictStr] = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
requested_changes: Optional[RequestedChanges] = # Replace with your value
entity_hrefs: Optional[StagedModificationsEntityHrefs] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
links: Optional[conlist(Link)] = None
staged_modification_instance = StagedModification(id=id, as_at_staged=as_at_staged, user_id_staged=user_id_staged, requested_id_staged=requested_id_staged, request_reason=request_reason, action=action, staging_rule=staging_rule, decisions=decisions, decisions_count=decisions_count, status=status, as_at_closed=as_at_closed, entity_type=entity_type, scope=scope, entity_unique_id=entity_unique_id, requested_changes=requested_changes, entity_hrefs=entity_hrefs, display_name=display_name, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

