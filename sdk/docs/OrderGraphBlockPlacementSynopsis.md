# OrderGraphBlockPlacementSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units placed. | 
**quantity_by_state** | **Dict[str, float]** | Total number of units placed. | [optional] 
**details** | [**List[OrderGraphBlockPlacementDetail]**](OrderGraphBlockPlacementDetail.md) | Identifiers for each placement in this block. | 

## Example

```python
from lusid.models.order_graph_block_placement_synopsis import OrderGraphBlockPlacementSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlockPlacementSynopsis from a JSON string
order_graph_block_placement_synopsis_instance = OrderGraphBlockPlacementSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlockPlacementSynopsis.to_json()

# convert the object into a dict
order_graph_block_placement_synopsis_dict = order_graph_block_placement_synopsis_instance.to_dict()
# create an instance of OrderGraphBlockPlacementSynopsis from a dict
order_graph_block_placement_synopsis_form_dict = order_graph_block_placement_synopsis.from_dict(order_graph_block_placement_synopsis_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


