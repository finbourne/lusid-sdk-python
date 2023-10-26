# PagedResourceListOfVirtualRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[VirtualRow]**](VirtualRow.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_virtual_row import PagedResourceListOfVirtualRow

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfVirtualRow from a JSON string
paged_resource_list_of_virtual_row_instance = PagedResourceListOfVirtualRow.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfVirtualRow.to_json()

# convert the object into a dict
paged_resource_list_of_virtual_row_dict = paged_resource_list_of_virtual_row_instance.to_dict()
# create an instance of PagedResourceListOfVirtualRow from a dict
paged_resource_list_of_virtual_row_form_dict = paged_resource_list_of_virtual_row.from_dict(paged_resource_list_of_virtual_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


