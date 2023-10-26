# OrderGraphPlacementOrderSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OrderGraphPlacementOrderDetail]**](OrderGraphPlacementOrderDetail.md) | Identifiers for each order in the block. | 

## Example

```python
from lusid.models.order_graph_placement_order_synopsis import OrderGraphPlacementOrderSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphPlacementOrderSynopsis from a JSON string
order_graph_placement_order_synopsis_instance = OrderGraphPlacementOrderSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphPlacementOrderSynopsis.to_json()

# convert the object into a dict
order_graph_placement_order_synopsis_dict = order_graph_placement_order_synopsis_instance.to_dict()
# create an instance of OrderGraphPlacementOrderSynopsis from a dict
order_graph_placement_order_synopsis_form_dict = order_graph_placement_order_synopsis.from_dict(order_graph_placement_order_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


