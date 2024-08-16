# WorkspaceItem

An item stored in a workspace.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the workspace item. | 
**format** | **int** | A simple integer format identifier. | 
**name** | **str** | A workspace item&#39;s name; a unique identifier. | 
**description** | **str** | The description of a workspace item. | 
**content** | **str** | The content associated with a workspace item. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.workspace_item import WorkspaceItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceItem from a JSON string
workspace_item_instance = WorkspaceItem.from_json(json)
# print the JSON string representation of the object
print WorkspaceItem.to_json()

# convert the object into a dict
workspace_item_dict = workspace_item_instance.to_dict()
# create an instance of WorkspaceItem from a dict
workspace_item_form_dict = workspace_item.from_dict(workspace_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


