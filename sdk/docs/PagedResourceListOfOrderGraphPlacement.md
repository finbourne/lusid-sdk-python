# PagedResourceListOfOrderGraphPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[OrderGraphPlacement]**](OrderGraphPlacement.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_order_graph_placement import PagedResourceListOfOrderGraphPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfOrderGraphPlacement from a JSON string
paged_resource_list_of_order_graph_placement_instance = PagedResourceListOfOrderGraphPlacement.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfOrderGraphPlacement.to_json()

# convert the object into a dict
paged_resource_list_of_order_graph_placement_dict = paged_resource_list_of_order_graph_placement_instance.to_dict()
# create an instance of PagedResourceListOfOrderGraphPlacement from a dict
paged_resource_list_of_order_graph_placement_form_dict = paged_resource_list_of_order_graph_placement.from_dict(paged_resource_list_of_order_graph_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


