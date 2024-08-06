# OrderGraphPlacementAllocationSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units allocated. | 
**details** | [**List[OrderGraphPlacementAllocationDetail]**](OrderGraphPlacementAllocationDetail.md) | Identifiers for each allocation in this placement. | 

## Example

```python
from lusid.models.order_graph_placement_allocation_synopsis import OrderGraphPlacementAllocationSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphPlacementAllocationSynopsis from a JSON string
order_graph_placement_allocation_synopsis_instance = OrderGraphPlacementAllocationSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphPlacementAllocationSynopsis.to_json()

# convert the object into a dict
order_graph_placement_allocation_synopsis_dict = order_graph_placement_allocation_synopsis_instance.to_dict()
# create an instance of OrderGraphPlacementAllocationSynopsis from a dict
order_graph_placement_allocation_synopsis_form_dict = order_graph_placement_allocation_synopsis.from_dict(order_graph_placement_allocation_synopsis_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


