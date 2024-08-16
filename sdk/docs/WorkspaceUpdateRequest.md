# WorkspaceUpdateRequest

A request to update a workspace.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A friendly description for the workspace. | 

## Example

```python
from lusid.models.workspace_update_request import WorkspaceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUpdateRequest from a JSON string
workspace_update_request_instance = WorkspaceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print WorkspaceUpdateRequest.to_json()

# convert the object into a dict
workspace_update_request_dict = workspace_update_request_instance.to_dict()
# create an instance of WorkspaceUpdateRequest from a dict
workspace_update_request_form_dict = workspace_update_request.from_dict(workspace_update_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


