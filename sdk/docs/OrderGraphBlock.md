# OrderGraphBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**ordered** | [**OrderGraphBlockOrderSynopsis**](OrderGraphBlockOrderSynopsis.md) |  | 
**placed** | [**OrderGraphBlockPlacementSynopsis**](OrderGraphBlockPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphBlockExecutionSynopsis**](OrderGraphBlockExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphBlockAllocationSynopsis**](OrderGraphBlockAllocationSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a block. | 
**derived_compliance_state** | **str** | The overall compliance state of a block, derived from the block&#39;s orders. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39; and &#39;Passed&#39;. | 

## Example

```python
from lusid.models.order_graph_block import OrderGraphBlock

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlock from a JSON string
order_graph_block_instance = OrderGraphBlock.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlock.to_json()

# convert the object into a dict
order_graph_block_dict = order_graph_block_instance.to_dict()
# create an instance of OrderGraphBlock from a dict
order_graph_block_form_dict = order_graph_block.from_dict(order_graph_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


