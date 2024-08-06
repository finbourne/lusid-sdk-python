# PagedResourceListOfAllocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Allocation]**](Allocation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_allocation import PagedResourceListOfAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfAllocation from a JSON string
paged_resource_list_of_allocation_instance = PagedResourceListOfAllocation.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfAllocation.to_json()

# convert the object into a dict
paged_resource_list_of_allocation_dict = paged_resource_list_of_allocation_instance.to_dict()
# create an instance of PagedResourceListOfAllocation from a dict
paged_resource_list_of_allocation_form_dict = paged_resource_list_of_allocation.from_dict(paged_resource_list_of_allocation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


