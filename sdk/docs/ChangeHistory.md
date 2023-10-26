# ChangeHistory

A group of changes made by the same person at the same time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier of the user that made the change. | 
**modified_as_at** | **datetime** | The date/time of the change. | 
**request_id** | **str** | The unique identifier of the request that the changes were part of. | 
**action** | **str** | The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete | 
**changes** | [**List[ChangeItem]**](ChangeItem.md) | The collection of changes that were made. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.change_history import ChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeHistory from a JSON string
change_history_instance = ChangeHistory.from_json(json)
# print the JSON string representation of the object
print ChangeHistory.to_json()

# convert the object into a dict
change_history_dict = change_history_instance.to_dict()
# create an instance of ChangeHistory from a dict
change_history_form_dict = change_history.from_dict(change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


