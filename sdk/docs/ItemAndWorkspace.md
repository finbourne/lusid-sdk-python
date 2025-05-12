# ItemAndWorkspace

An item plus its containing workspace name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_name** | **str** | A workspace&#39;s name. | 
**workspace_item** | [**WorkspaceItem**](WorkspaceItem.md) |  | 

## Example

```python
from lusid.models.item_and_workspace import ItemAndWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAndWorkspace from a JSON string
item_and_workspace_instance = ItemAndWorkspace.from_json(json)
# print the JSON string representation of the object
print ItemAndWorkspace.to_json()

# convert the object into a dict
item_and_workspace_dict = item_and_workspace_instance.to_dict()
# create an instance of ItemAndWorkspace from a dict
item_and_workspace_form_dict = item_and_workspace.from_dict(item_and_workspace_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


