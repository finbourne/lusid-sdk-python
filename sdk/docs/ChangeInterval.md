# ChangeInterval

Defines a change that occured for an entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The date/time of the change. | [optional] 
**user_id_modified** | **str** | The unique identifier of the user that made the change. | [optional] 
**request_id_modified** | **str** | The unique identifier of the request that the changes were part of. | [optional] 
**as_at_version_number** | **int** | The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself. | [optional] 
**staged_modification_id_modified** | **str** | The id of the staged modification that was approved. Will be null if the change didn&#39;t come from a staged modification. | [optional] 
**action** | **str** | The action performed on the entity. | [optional] 
**attribute_name** | **str** | The name of the field or property that has been changed. | [optional] 
**previous_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**new_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effective_range** | [**EffectiveRange**](EffectiveRange.md) |  | [optional] 

## Example

```python
from lusid.models.change_interval import ChangeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeInterval from a JSON string
change_interval_instance = ChangeInterval.from_json(json)
# print the JSON string representation of the object
print ChangeInterval.to_json()

# convert the object into a dict
change_interval_dict = change_interval_instance.to_dict()
# create an instance of ChangeInterval from a dict
change_interval_form_dict = change_interval.from_dict(change_interval_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


