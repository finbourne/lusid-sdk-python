# OrderGraphPlacementPlacementSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OrderGraphPlacementChildPlacementDetail]**](OrderGraphPlacementChildPlacementDetail.md) | Identifiers for each child placement for this placement. | 
**quantity** | **float** | Total number of units placed. | 

## Example

```python
from lusid.models.order_graph_placement_placement_synopsis import OrderGraphPlacementPlacementSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphPlacementPlacementSynopsis from a JSON string
order_graph_placement_placement_synopsis_instance = OrderGraphPlacementPlacementSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphPlacementPlacementSynopsis.to_json()

# convert the object into a dict
order_graph_placement_placement_synopsis_dict = order_graph_placement_placement_synopsis_instance.to_dict()
# create an instance of OrderGraphPlacementPlacementSynopsis from a dict
order_graph_placement_placement_synopsis_form_dict = order_graph_placement_placement_synopsis.from_dict(order_graph_placement_placement_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


