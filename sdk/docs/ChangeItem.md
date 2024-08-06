# ChangeItem

Information about a change to a field / property.  At least one of 'PreviousValue' or 'NewValue' will be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field or property that has been changed. | 
**previous_value** | **str** | The previous value for this field / property. | [optional] 
**new_value** | **str** | The new value for this field / property. | [optional] 
**effective_from** | **datetime** | The market data time, i.e. the time to run the change from. | [optional] 
**effective_until** | **datetime** | The market data time, i.e. the time to run the change until. | [optional] 

## Example

```python
from lusid.models.change_item import ChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeItem from a JSON string
change_item_instance = ChangeItem.from_json(json)
# print the JSON string representation of the object
print ChangeItem.to_json()

# convert the object into a dict
change_item_dict = change_item_instance.to_dict()
# create an instance of ChangeItem from a dict
change_item_form_dict = change_item.from_dict(change_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


