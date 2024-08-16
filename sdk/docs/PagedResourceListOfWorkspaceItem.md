# PagedResourceListOfWorkspaceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[WorkspaceItem]**](WorkspaceItem.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_workspace_item import PagedResourceListOfWorkspaceItem

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfWorkspaceItem from a JSON string
paged_resource_list_of_workspace_item_instance = PagedResourceListOfWorkspaceItem.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfWorkspaceItem.to_json()

# convert the object into a dict
paged_resource_list_of_workspace_item_dict = paged_resource_list_of_workspace_item_instance.to_dict()
# create an instance of PagedResourceListOfWorkspaceItem from a dict
paged_resource_list_of_workspace_item_form_dict = paged_resource_list_of_workspace_item.from_dict(paged_resource_list_of_workspace_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


