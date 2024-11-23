# WorkspaceCreationRequest

A request to create an empty workspace.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A workspace&#39;s name. | 
**description** | **str** | A friendly description for the workspace. | 

## Example

```python
from lusid.models.workspace_creation_request import WorkspaceCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreationRequest from a JSON string
workspace_creation_request_instance = WorkspaceCreationRequest.from_json(json)
# print the JSON string representation of the object
print WorkspaceCreationRequest.to_json()

# convert the object into a dict
workspace_creation_request_dict = workspace_creation_request_instance.to_dict()
# create an instance of WorkspaceCreationRequest from a dict
workspace_creation_request_form_dict = workspace_creation_request.from_dict(workspace_creation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


