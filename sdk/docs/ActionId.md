# ActionId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**activity** | **str** |  | 
**entity** | **str** |  | 

## Example

```python
from lusid.models.action_id import ActionId

# TODO update the JSON string below
json = "{}"
# create an instance of ActionId from a JSON string
action_id_instance = ActionId.from_json(json)
# print the JSON string representation of the object
print ActionId.to_json()

# convert the object into a dict
action_id_dict = action_id_instance.to_dict()
# create an instance of ActionId from a dict
action_id_form_dict = action_id.from_dict(action_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


