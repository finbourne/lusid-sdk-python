# PagedResourceListOfPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Placement]**](Placement.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_placement import PagedResourceListOfPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfPlacement from a JSON string
paged_resource_list_of_placement_instance = PagedResourceListOfPlacement.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfPlacement.to_json()

# convert the object into a dict
paged_resource_list_of_placement_dict = paged_resource_list_of_placement_instance.to_dict()
# create an instance of PagedResourceListOfPlacement from a dict
paged_resource_list_of_placement_form_dict = paged_resource_list_of_placement.from_dict(paged_resource_list_of_placement_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


