# OrderGraphBlockAllocationSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units allocated. | 
**details** | [**List[OrderGraphBlockAllocationDetail]**](OrderGraphBlockAllocationDetail.md) | Identifiers for each allocation in this block. | 

## Example

```python
from lusid.models.order_graph_block_allocation_synopsis import OrderGraphBlockAllocationSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlockAllocationSynopsis from a JSON string
order_graph_block_allocation_synopsis_instance = OrderGraphBlockAllocationSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlockAllocationSynopsis.to_json()

# convert the object into a dict
order_graph_block_allocation_synopsis_dict = order_graph_block_allocation_synopsis_instance.to_dict()
# create an instance of OrderGraphBlockAllocationSynopsis from a dict
order_graph_block_allocation_synopsis_form_dict = order_graph_block_allocation_synopsis.from_dict(order_graph_block_allocation_synopsis_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


