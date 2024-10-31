# WorkspaceItemUpdateRequest

A request to update a workspace item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **int** | A simple integer format identifier. | 
**description** | **str** | The description of a workspace item. | 
**content** | **object** | The content associated with a workspace item. | 
**type** | **str** | The type of the workspace item. | 

## Example

```python
from lusid.models.workspace_item_update_request import WorkspaceItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceItemUpdateRequest from a JSON string
workspace_item_update_request_instance = WorkspaceItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print WorkspaceItemUpdateRequest.to_json()

# convert the object into a dict
workspace_item_update_request_dict = workspace_item_update_request_instance.to_dict()
# create an instance of WorkspaceItemUpdateRequest from a dict
workspace_item_update_request_form_dict = workspace_item_update_request.from_dict(workspace_item_update_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


