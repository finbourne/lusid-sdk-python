# PagedResourceListOfItemAndWorkspace


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ItemAndWorkspace]**](ItemAndWorkspace.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_item_and_workspace import PagedResourceListOfItemAndWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfItemAndWorkspace from a JSON string
paged_resource_list_of_item_and_workspace_instance = PagedResourceListOfItemAndWorkspace.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfItemAndWorkspace.to_json()

# convert the object into a dict
paged_resource_list_of_item_and_workspace_dict = paged_resource_list_of_item_and_workspace_instance.to_dict()
# create an instance of PagedResourceListOfItemAndWorkspace from a dict
paged_resource_list_of_item_and_workspace_form_dict = paged_resource_list_of_item_and_workspace.from_dict(paged_resource_list_of_item_and_workspace_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


