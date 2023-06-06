# OrderGraphPlacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement** | [**Placement**](Placement.md) |  | 
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**ordered** | [**OrderGraphPlacementOrderSynopsis**](OrderGraphPlacementOrderSynopsis.md) |  | 
**placed** | [**OrderGraphPlacementPlacementSynopsis**](OrderGraphPlacementPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphPlacementExecutionSynopsis**](OrderGraphPlacementExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphPlacementAllocationSynopsis**](OrderGraphPlacementAllocationSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a placement. | 
**calculated_average_price** | **float** | Average price realised on executions for a given placement | [optional] 

## Example

```python
from lusid.models.order_graph_placement import OrderGraphPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphPlacement from a JSON string
order_graph_placement_instance = OrderGraphPlacement.from_json(json)
# print the JSON string representation of the object
print OrderGraphPlacement.to_json()

# convert the object into a dict
order_graph_placement_dict = order_graph_placement_instance.to_dict()
# create an instance of OrderGraphPlacement from a dict
order_graph_placement_form_dict = order_graph_placement.from_dict(order_graph_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


