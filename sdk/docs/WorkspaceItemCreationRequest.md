# WorkspaceItemCreationRequest

A request to create an item in a workspace.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **int** | A simple integer format identifier. | 
**name** | **str** | A workspace item&#39;s name. | 
**group** | **str** | The group containing a workspace item. | 
**description** | **str** | The description of a workspace item. | 
**content** | **object** | The content associated with a workspace item. | 
**type** | **str** | The type of the workspace item. | 

## Example

```python
from lusid.models.workspace_item_creation_request import WorkspaceItemCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceItemCreationRequest from a JSON string
workspace_item_creation_request_instance = WorkspaceItemCreationRequest.from_json(json)
# print the JSON string representation of the object
print WorkspaceItemCreationRequest.to_json()

# convert the object into a dict
workspace_item_creation_request_dict = workspace_item_creation_request_instance.to_dict()
# create an instance of WorkspaceItemCreationRequest from a dict
workspace_item_creation_request_form_dict = workspace_item_creation_request.from_dict(workspace_item_creation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


