# Version

The version metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** | The effective datetime at which this version became valid. Only applies when a single entity is being interacted with. | 
**as_at_date** | **datetime** | The asAt datetime at which the data was committed to LUSID. | 
**as_at_created** | **datetime** | The asAt datetime at which the entity was first created in LUSID. | [optional] [readonly] 
**user_id_created** | **str** | The unique id of the user who created the entity. | [optional] [readonly] 
**as_at_modified** | **datetime** | The asAt datetime at which the entity (including its properties) was last updated in LUSID. | [optional] [readonly] 
**user_id_modified** | **str** | The unique id of the user who last updated the entity (including its properties) in LUSID. | [optional] [readonly] 
**as_at_version_number** | **int** | The integer version number for the entity (the entity was created at version 1) | [optional] [readonly] 

## Example

```python
from lusid.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print Version.to_json()

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_form_dict = version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


