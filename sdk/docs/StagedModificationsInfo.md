# StagedModificationsInfo

The staged modifications metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_pending** | **int** | The number of staged modifications for the entity with a status of Pending for the requested asAt. | 
**href_pending** | **str** | Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (&#x3D; Pending). | 
**ids_previewed** | **List[str]** | An array of the ids of any StagedModifications being previewed. | [optional] 

## Example

```python
from lusid.models.staged_modifications_info import StagedModificationsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationsInfo from a JSON string
staged_modifications_info_instance = StagedModificationsInfo.from_json(json)
# print the JSON string representation of the object
print StagedModificationsInfo.to_json()

# convert the object into a dict
staged_modifications_info_dict = staged_modifications_info_instance.to_dict()
# create an instance of StagedModificationsInfo from a dict
staged_modifications_info_form_dict = staged_modifications_info.from_dict(staged_modifications_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


