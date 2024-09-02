# EntityChangeItem

Defines a change that occured for an entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The date/time of the change. | 
**user_id_modified** | **str** | The unique identifier of the user that made the change. | 
**request_id_modified** | **str** | The unique identifier of the request that the changes were part of. | 
**as_at_version_number** | **int** | The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself. | 
**action** | **str** | The action performed on the entity. | 
**action_description** | **str** | Description of the action performed on the entity. | 
**attribute_name** | **str** | The name of the field or property that has been changed. | [optional] 
**previous_value** | **object** | The value of the attribute prior to the change. | [optional] 
**new_value** | **object** | The value of the attribute following the change. | [optional] 
**effective_from** | **datetime** | The effective datetime from which the field&#39;s new value is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the field&#39;s new value is valid. | [optional] 
**detail** | **Dict[str, str]** | Information about the particular instance of the ChangeItem (supplied information depends on the type of Action). | [optional] 

## Example

```python
from lusid.models.entity_change_item import EntityChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of EntityChangeItem from a JSON string
entity_change_item_instance = EntityChangeItem.from_json(json)
# print the JSON string representation of the object
print EntityChangeItem.to_json()

# convert the object into a dict
entity_change_item_dict = entity_change_item_instance.to_dict()
# create an instance of EntityChangeItem from a dict
entity_change_item_form_dict = entity_change_item.from_dict(entity_change_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


