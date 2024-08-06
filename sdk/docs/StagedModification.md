# StagedModification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Id for the staged modification | [optional] 
**as_at_staged** | **datetime** | Time at which the modification was staged. | [optional] 
**user_id_staged** | **str** | Id of the user who created the stage modification request. | [optional] 
**requested_id_staged** | **str** | The Request Id that initiated this staged modification. | [optional] 
**action** | **str** | Type of action of the staged modification, either create, update or delete. | [optional] 
**staging_rule** | [**StagedModificationStagingRule**](StagedModificationStagingRule.md) |  | [optional] 
**decisions** | [**List[StagedModificationDecision]**](StagedModificationDecision.md) | Object containing information relating to the decision on the staged modification. | [optional] 
**decisions_count** | **int** | Number of decisions made. | [optional] 
**status** | **str** | The status of the staged modification. | [optional] 
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

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModification from a JSON string
staged_modification_instance = StagedModification.from_json(json)
# print the JSON string representation of the object
print StagedModification.to_json()

# convert the object into a dict
staged_modification_dict = staged_modification_instance.to_dict()
# create an instance of StagedModification from a dict
staged_modification_form_dict = staged_modification.from_dict(staged_modification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


